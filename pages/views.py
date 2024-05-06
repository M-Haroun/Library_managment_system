from django.shortcuts import render
from books.models import Book, Category
from random import sample

# Create your views here.

def index(request):
    Book_data=Book.objects.all()
    Cat_data=Category.objects.all()
    Cat_random = sample(list(Cat_data), 5)
    return render(request,'pages/index.html',{'books':Book_data,'categories':Cat_data,
                                              'random_categories':Cat_random})