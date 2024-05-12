from django.shortcuts import render
from books.models import Book, Category
from books.forms import BookForm, CategoryForm
from random import sample

# Create your views here.

def index(request):
    Book_data=Book.objects.all()
    Cat_data=Category.objects.all()
    Cat_random = sample(list(Cat_data), 5)
    Book_form=BookForm()
    
    if request.method == 'POST':
        BookForm_data = BookForm(request.POST, request.FILES)
        if BookForm_data.is_valid():
            BookForm_data.save() 
    
    context = {'books':Book_data,
               'categories':Cat_data,
               'random_categories':Cat_random,
               'bookform':Book_form,
               }
    return render(request,'pages/index.html',context)