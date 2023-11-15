from nz.views import *
from django.urls import path

app_name = 'World cup'

urlpatterns = [
    path('williamson/',williamson,name='williamson'),
    path('mitchill/',mitchill,name='mitchill'),
    
]