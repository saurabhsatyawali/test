from django.shortcuts import render,HttpResponse

from django.db import connection
from django.db.models import Avg
from datetime import date
from kj.models import Author
# Create your views here.
def demo(request):
 a=Author.objects.get(pk=1)
 print(a.kj_book.all())



 return HttpResponse("ok")

 # print(connection.queries)
















