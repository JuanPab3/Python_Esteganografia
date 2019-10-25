from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
        'author':'Juan P. Sierra',
        'title':'My Birthday',
        'content':'Happy birthday Jp',
        'date_posted':'May 24 2018',
    },
    {
        'author':'Juan P. Sierra',
        'title':'My Birthday Yesterday',
        'content':'Not my birthday anymore.',
        'date_posted':'May 25 2018',
    }

]

def home(request):
    context = {
        'posts' : posts
    }
    return render(request, "blog/home.html", context)

def about(request):
    content = {
        'title': "about"
    }
    return render(request, "blog/about.html", content)
