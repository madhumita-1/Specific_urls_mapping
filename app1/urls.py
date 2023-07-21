from django.urls import path
from app1.views import *
app1_name='hello'

urlpatterns=[
 path('first/',first,name='first'),   
]