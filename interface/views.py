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
        a = urlopen(image_path).read()
        img = Image.frombytes('RGB', (200, 00), data,
                              decoder_name='raw', *args)
        # image = NamedTemporaryFile()
        # image.write()
        # image.flush()
        # a = File(image)
        # a.sa
        # #.write('/Users/d.s.zubov/Desktop/Курсовая/djangoProject/interface/static/test1.jpg')
        # print(type())
        # name = str(image.name).split('\\')[-1]
        # name += '.jpg'  # store image in jpeg format
        # image.name = name
        return render(request, 'result.html', context=context)
    return render(request, 'index.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'.

def show_result(request):
    return render(request, 'result.html')
