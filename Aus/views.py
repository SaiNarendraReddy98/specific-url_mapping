from django.shortcuts import render

# Create your views here.
def warner(request):
    return render(request,'warner.html')

