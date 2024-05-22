from django.shortcuts import render
from .models import Book, Category
from .forms import CategoryForm

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
