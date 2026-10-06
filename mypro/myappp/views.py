from django.shortcuts import render

# # Create your views here.
from django.http import HttpResponse
#
# #function based
#
# def first(request):
#     return HttpResponse("First page")
#
# def second(request):
#     return HttpResponse("Second Page")

##Class Based

from django.views import View

from myappp.models import Person


# class First(View):
#     def get(self, request):
#         return HttpResponse("""
#         <h1>First page</h1>
#         <h1>hello</h1>""")
#
# class Second(View):
#     def get(self, request):
#         return HttpResponse("<h1>Second page</h1>")
from myappp.models import Person
class First(View):
    def get(self, request):

        # data=[{"name":"Aadhil","age":21,"place":"alp"},
        #       {"name":"Aman","age":23,"place":"ekm"},
        #       {"name":"Akhilesh","age":21,"place":"alp"}]

        data=Person.objects.all()

        context = {"data":data}

        return render(request, 'first.html',context)

class Second(View):
    def get(self, request):
        data = {"name": "Akhilesh", "age": 21, "place": "alp"}
        return render(request, 'second.html',context=data)

from myappp.models import Movie
class Movie_list(View):
    def get(self,request):
        data=Movie.objects.all()
        context = {'data': data}
        return render(request, 'movie.html', context)

class Add_movie(View):
    def get(self,request):
        return render(request, 'addmovie.html')
    def post(self,request):
        print(request.POST)   #submitted data

        data=request.POST
        n=data['name']
        d=data['director']
        y=data['year']
        print(n,d,y)

        # insert into movie(name,director,year)values

        m=Movie.objects.create(movie_name=n,director=d,year=y)
        m.save()
        return render(request, 'addmovie.html')