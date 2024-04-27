from django.shortcuts import render
from books.models import Book, Category
# Create your views here.

def index(request):
    Book_data=Book.objects.all()
    Cat_data=Category.objects.all()
    return render(request,'pages/index.html',{'books':Book_data,'categories':Cat_data})