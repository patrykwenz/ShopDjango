from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_view(request):
    return render(request, "shop_views/base.html", {})


def about_view(request):
    return HttpResponse('<h1> About </h1>')
