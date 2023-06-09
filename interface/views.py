# Import these methods
import binascii
from urllib.request import urlopen
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import redirect, render
from interface.models import myImage
from PIL import Image
import os
from interface.myCode import model

def image_upload(request):
    context = dict()
    if request.method == 'POST':
        image_path = request.POST["src"]  # src is the name of input attribute in your html file, this src value is set in javascript code
        with open('/Users/d.s.zubov/Desktop/Курсовая/djangoProject/interface/static/imageBase64.txt', 'w') as f:
            f.write(image_path)
        print('1')
        with open("/Users/d.s.zubov/Desktop/Курсовая/djangoProject/interface/static/test.jpg", "wb") as binary_file:
            # Write bytes to file
            binary_file.write(urlopen(image_path).read())
        pred = model()
        context['style'] = pred[0]
        context['images'] = pred[1]
        # image = NamedTemporaryFile()
        # image.write(urlopen(image_path).read())
        # image.flush()
        # image = File(image)
        # name = str(image.name).split('\\')[-1]
        # name += '.jpg'  # store image in jpeg format
        # image.name = name
        # if image is not None:
        #     obj = myImage.objects.create(image=image)  # create a object of Image type defined in your model
        #     obj.save()
        return render(request, 'result.html', context=context)
    return render(request, 'index.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.

def show_result(request):
    return render(request, 'result.html')
