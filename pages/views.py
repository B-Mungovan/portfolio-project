from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.clickjacking import xframe_options_exempt

def home(request):
   return render(request, 'pages/index.html')

def contact(request):
   return render(request, 'pages/contact_me.html')

def navbar(request):
   return render(request, 'pages/navbar.html')   

def my_cv(request):
   return render(request, 'pages/my_cv.html')

@xframe_options_exempt
def ok_to_load_in_a_frame(request):
    return HttpResponse("pages/my_cv.html")