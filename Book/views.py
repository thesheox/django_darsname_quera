from django.shortcuts import render
from django.http import HttpResponse

from Book.models import Author


def say_hello(request,first_name):
    return HttpResponse(f"Hello {first_name}")

def author(request):
    author=Author(name="hasan")
    return HttpResponse(author.name)

