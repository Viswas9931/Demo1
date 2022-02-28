# import requests
# from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def demo(request):
    return render(request, "index.html")


def addition(request):
    x = int(request.GET['num1'])
    y = int(request.GET['num2'])
    res=x-y,x+y,x/y,x*y
    return render(request, "about.html",{'about':res})



# def about(request):
#     return render(request,"about.html")
#
# def contact(request):
#     return render(request,"contact.html")
#
# def details(request):
#     return HttpResponse("hello im details")
#
# def thanks(request):
#     return HttpResponse("hello im thanks")
