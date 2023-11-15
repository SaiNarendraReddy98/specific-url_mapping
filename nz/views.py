from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def williamson(request):
    return render(request,'williamson.html')

def mitchill(request):
    return HttpResponse('<center> <h1 style="color:green",> Best Batsman in ODI with 131 scored in the ODI 2023')
