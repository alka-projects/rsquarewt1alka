from django.shortcuts import render
from django.http import HttpResponse
import time

# Create your views here.
def home(request):
    return render(request,'rsquare/initiation.html',{'range':'0'})

def range_view(request,range1):
    range1=range1
    range1=int(range1)
    if range1==0:
        # return render(request,'rsquare/home.html',{'range':range1})
        return render(request,'rsquare/initiation.html',{'range':range1})
    elif range1==34:
        return render(request,'rsquare/planning.html',{'range':range1})
    elif range1==67:
        return render(request,'rsquare/execution.html',{'range':range1})
    elif range1==100:
        return render(request,'rsquare/closing.html',{'range':range1})





# def initiation_view(request):
#     return render(request,'rsquare/initiation.html')
#
# def planning_view(request):
#     return render(request,'rsquare/planning.html')
#
# def execution_view(request):
#     return render(request,'rsquare/execution.html')
#
# def closing_view(request):
#     return render(request,'rsquare/closing.html')
#
def cart_view(request):
    return render(request,'rsquare/cart.html')

def final_view(request):
    return render(request,'rsquare/final.html')
