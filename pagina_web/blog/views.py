from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse(
"""
<h1>Blog Home</h1>
<h3> Solo quiero saber si esto tiene sentido</h3>
""")

def about(request):
    return HttpResponse(
"""
<h1>Blog About</h1>
<h3> Solo quiero saber si esto tiene sentido</h3>
""")
