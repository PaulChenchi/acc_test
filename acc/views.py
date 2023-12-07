from django.shortcuts import render
from django.http import HttpResponse #專門封裝資訊透過他傳遞
from django.contrib.auth.forms import UserCreationForm  # django 內建表單模組
from django.contrib.auth.models import User
# Create your views here.
# 寫功能的地方

def slaes_data(request):
    # return HttpResponse("<h1>Welcome to Acc_sales APP")

    return render(request,"acc/sales_data.html") 


def resgister(request):
    message=''
    if request.method=="POST":
        print(request.POST)
        username=request.POST["username"]
        password1=request.POST["password1"]
        password2=request.POST["password2"]

        print(username,password1,password2)
        if password1!=password2:
            message='密碼不相同'
        elif len(password1)<8:
            message='密碼太短了'

    form=UserCreationForm()
    return render(request,"acc/resgister.html",{"form":form,"message":message})