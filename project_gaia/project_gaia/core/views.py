from urllib import request
# from django.http import HttpRequest 
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html'
)

from django.http import HttpResponse

def home(request):
    from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')



from django.shortcuts import render

def home(request):
    return render(request, 'core/home.html')  # 👈 Must match file path
