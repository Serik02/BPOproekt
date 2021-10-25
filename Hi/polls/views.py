from urllib import request

from django.shortcuts import render


# Create your views here.
def main(request):
    return render(request, "index.html")


def salam(request):
    return render(request, 'salam.html')