import binascii
from urllib.request import urlopen
from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import redirect, render
from interface.models import myImage
from PIL import Image
import os
from interface.predict_model import model


def image_upload(request):
    context = dict()
    if request.method == 'POST':
        image_path = request.POST["src"]
        with open("./interface/static/taked_photo.jpg", "wb") as binary_file:
            binary_file.write(urlopen(image_path).read())
        pred = model(size=200, d=11, k=50, num_resp_imgs=12, database_name="database_learn_200_11.csv")
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
        #     obj = myImage.objects.create(image=image)
        #     obj.save()
        return render(request, 'result.html', context=context)
    return render(request, 'home.html', context=context)


def show_result(request):
    return render(request, 'result.html')
