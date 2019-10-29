from django.shortcuts import render
from .esteganew import Esteganew
from django.core.files.storage import FileSystemStorage

def home(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['pre_esteganew']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        print(url)
        boop = Esteganew(fs, url,"perrito","mango")
        boop.codificar()


    return render(request, "esteganew/home.html")

def about(request):
        return render(request, "esteganew/about.html", {'title': 'About'})
