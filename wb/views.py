from django.shortcuts import render
from .models import ModelTable

# Create your views here.

def index(request):
    data  =  ModelTable.objects.all()

    context = {
        "data": data
    }
    return render(request,'index.html',context)