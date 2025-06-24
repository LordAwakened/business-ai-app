from django.urls import path
from . views import index
appname = 'core'
urlpatterns =[
    path('core/',index, name= 'index')
]