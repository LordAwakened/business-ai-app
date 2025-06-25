from django.urls import path
from . views import index
appname = 'core'
urlpatterns =[
    path('core/',index, name= 'index')
]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
