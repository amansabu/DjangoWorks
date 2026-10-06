from django.db.models import Model
from django.http import HttpResponse,JsonResponse

from django.shortcuts import render
from django.views import View
# Create your views here.

class GoodMorning(View):
    def get(self, request):
        data={"message": "Good Morning"}
        return JsonResponse(data)


class HelloWorld(View):
    def get(self, request):
        data={"message": "Hello World"}
        return JsonResponse(data)


class GoodEvening(View):
    def get(self, request):
        data={"message": "Good Evening"}
        return JsonResponse(data)

class UserDetails(View):
    def get(self,request):
        data=[{'name':'Aman','Age':23,'place':'ekm'},
              {'name':'Adhil','Age':22,'place':'alp'},
              {'name':'Alby','Age':21,'place':'idukki'}]

        return JsonResponse(data,safe=False)

from myapp.models import Student

class StudentList(View):
    def get(self,request):
        s=Student.objects.all().values()
        print(s)
        print(type(s))

        data=list(s)
        print(data)
        print(type(data))

        return jsonResponse(data,safe=False)
