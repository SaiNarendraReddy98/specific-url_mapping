from india.views import *
from django.urls import path

app_name='lokeshchatta'

urlpatterns = [

    path('rohit/',rohit,name='rohit'),
    path('virat/',virat,name='virat'),
    path('mdshami/',mdshami,name='mdshami'),
    


]