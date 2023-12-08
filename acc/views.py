from django.shortcuts import render,redirect # redirect重新導向網頁
from django.http import HttpResponse #專門封裝資訊透過他傳遞
from django.contrib.auth.forms import UserCreationForm  # django 內建表單模組
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate #authenticate 內建登入
# Create your views here.
# 寫功能的地方


def acc_login(request):
    message=''
    if request.method=="POST":
        if request.POST.get("register"):# template 按鈕
            return redirect("register") #urls 
        elif request.POST.get("login"):
            print("login")
            username = request.POST["username"]
            password = request.POST["password"]
            user = User.objects.filter(username=username)
            if not user:
                message="沒有這個帳號！"
            else:
                user = authenticate(request,username=username,password=password)
                if not user:
                    message="密碼錯誤！"
                else:
                    login(request,user) # authenticate紀錄登入
                    message="登入成功！"
        print(user)
            
    return render(request,"acc/login.html",{"message":message})

def sales_data(request):
    # return HttpResponse("<h1>Welcome to Acc_sales APP")

    return render(request,"acc/sales_data.html") 


def register(request):
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
        else:
            #確認帳號是否重複
            if User.objects.filter(username=username):
                message='帳號已存在'
            else:
                # 建立使用者
                user=User.objects.create_user(username=username,password=password1)
                user.save()
                message='註冊成功！'

    form=UserCreationForm()
    return render(request,"acc/register.html",{"form":form,"message":message})