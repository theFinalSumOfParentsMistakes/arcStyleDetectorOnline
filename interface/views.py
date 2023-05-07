# Import these methods
from urllib.request import urlopen

from django.core.files import File
from django.core.files.base import ContentFile
from django.core.files.temp import NamedTemporaryFile
from django.shortcuts import redirect, render
from interface.models import Image


def image_upload(request):
    context = dict()
    if request.method == 'POST':
        username = request.POST["username"]
        path = request.POST["src"]  # src is the name of input attribute in your html file, this src value is set in javascript code
        image = NamedTemporaryFile()
        image.write(urlopen(path).read())
        image.flush()
        image = File(image)
        name = str(image.name).split('\\')[-1]
        name += '.jpg'  # store image in jpeg format
        image.name = name
        if image is not None:
            obj = Image.objects.create(username=username, image=image)  # create a object of Image type defined in your model
            obj.save()
            context["path"] = obj.image.url  #url to image stored in my server/local device
            context["username"] = obj.username
        else :
            return redirect('/')
        return redirect('any_url')
    return render(request, 'index.html', context=context)  # context is like respose data we are sending back to user, that will be rendered with specified 'html file'. 