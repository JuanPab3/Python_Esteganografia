from django.shortcuts import render

def home(request):
    return render(request, "esteganew/home.html")

def about(request):
    return render(request, "esteganew/about.html", {'title': 'About'})
