from django.urls import path
from Aus.views import *

app_name = 'sai'

urlpatterns = [
    path('warner/',warner,name='warner'),
    
]