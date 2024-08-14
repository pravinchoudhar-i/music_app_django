from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentRegistration
from .models import User



#Create your views here.
def Lenovo(request):
           
    return render(request,'index.html')

def Temp(request):
    return render(request,'temp.html')


    