from django.shortcuts import render,redirect
from .models import Book, Category
from .forms import CategoryForm, BookForm
from pages.views import update,delete

# Create your views here.
def books(request):
    Book_data=Book.objects.all()
    Cat_data=Category.objects.all()
    Category_form=CategoryForm()
    
    if request.method == 'POST':      
        Category_data = CategoryForm(request.POST)
        if Category_data.is_valid():
            Category_data.save()
             
    context = {'books':Book_data,
               'categories':Cat_data,
               'categoryform':Category_form,
               }
    return render(request,"books/books.html",context)

def update_book(request, id):
    return update(request, id,'books')

def delete_book(request, id):
    return delete(request, id,'books')
    