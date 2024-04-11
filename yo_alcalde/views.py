from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "yo_alcalde/base.html")


def login(request):
    return render(request, "yo_alcalde/login.html")
