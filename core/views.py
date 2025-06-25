from django.shortcuts import render



# Create your views here.


from django.http import HttpResponse

def home(request):
   from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')

from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')  # 👈 Must match file path
