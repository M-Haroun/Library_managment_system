from django.shortcuts import render
from books.models import Book, Category

# Create your views here.
def books(request):
    Book_data=Book.objects.all()
    return render(request,"books/books.html",{'books':Book_data})
