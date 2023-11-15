from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def rohit(request):
    return render(request,'rohit.html')

def virat(request):
    return HttpResponse('<h1> <center> 50th ODI century Best Batsman in INDIA ')

def mdshami(request):
    return HttpResponse('<center> <h1 style="color:blue",> Best bowler in ODI with highest wicket taken in the ODI 2023')
