from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def goodf(request):
    # return HttpResponse("文采经济")
    return render(request,'goode.html')