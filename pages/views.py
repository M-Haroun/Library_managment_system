from django.shortcuts import render
from books.models import Book
# Create your views here.

def index(request):
    data=Book.objects.all()
    return render(request,'pages/index.html',{'books':data})