from django.shortcuts import render
from django.http import HttpResponse #專門封裝資訊透過他傳遞

# Create your views here.
# 寫功能的地方

def slaes_data(request):
    # return HttpResponse("<h1>Welcome to Acc_sales APP")

    return render(request,"acc/sales_data.html") 