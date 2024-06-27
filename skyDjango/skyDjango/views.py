from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("Hello world this is Django home page")
    return render(request, 'website/index.html')
def about(request):
    return HttpResponse("Hello world this is Django about page")
def contact(request):
    return HttpResponse("Hello world this is Django contact page") 