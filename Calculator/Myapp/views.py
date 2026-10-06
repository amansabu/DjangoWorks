import math
from difflib import context_diff

from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from django.views import View




class Home(View):
    def get(self, request):

        return render(request,'home.html')

class Add(View):
    def get(self,request):
        return  render(request,'add.html')
    def post(self,request):
        data=request.POST
        n1=int(data['n1'])
        n2=int(data['n2'])

        s=n1+n2
        print(s)
        context={'result':s}

        return render(request,'add.html',context)

class Fact(View):
    def get(self,request):
        return render(request,'fact.html')
    def post(self,request):
        data=request.POST
        n=int(data['n'])
        f=math.factorial(n)
        print(f)
        context={'result':f}
        return render(request,'fact.html',context)

class Bmi(View):
    def get(self,request):
        return render(request,'bmi.html')
    def post(self,request):
        data=request.POST
        n=int(data['n'])
        b=float(data['b'])
        m=n/b**2
        print(m)
        context={'result':m}
        return render(request,'bmi.html',context)

