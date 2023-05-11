# Import these methods
from urllib.request import urlopen
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import redirect, render
from interface.models import myImage
from PIL import Image
import os


def image_upload(request):
    context = dict()
    if request.method == 'POST':
        path = request.POST["src"]
        image = NamedTemporaryFile()
        image.write(urlopen(path).read())
        image.flush()
        image = File(image)
        obj = myImage.objects.create(image=image)
        obj.save()
        #
        # path = request.POST["src"]  # src is the name of input attribute in your html file, this src value is set in javascript code
        # image = NamedTemporaryFile()
        # # #image.write(urlopen(path).read())
        # # image.flush()
        # image = File(image)
        # image.write
        # os.mkdir('./interface/static/1.jpg', image)
        # image = Image.Image(image)
        # image.save('./interface/static/1.jpg')
        # # name = str(image.name).split('\\')[-1]
        # # name += '.jpg'  # store image in jpeg format
        # # image.name = name
        # # if image is not None:
        # #     obj = Image.objects.create(image=image)  # create a object of Image type defined in your model
        # #     obj.save()
        # #     context["path"] = obj.image.url  #url to image stored in my server/local device
        # # else:
        # #     return render(request, 'result.html')
        return render(request, 'result.html')
    return render(request, 'index.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.

def show_result(request):
    return render(request, 'result.html')
