from django.shortcuts import render,redirect, get_object_or_404
from books.models import Book, Category
from books.forms import BookForm, CategoryForm
from random import sample

# Create your views here.

def index(request):
    Book_data=Book.objects.all()
    Cat_data=Category.objects.all()
    Cat_random = sample(list(Cat_data), 5)
    Book_form=BookForm()
    Category_form=CategoryForm()
    
    if request.method == 'POST':
        BookForm_data = BookForm(request.POST, request.FILES)
        if BookForm_data.is_valid():
            BookForm_data.save() 
                
        Category_data = CategoryForm(request.POST)
        if Category_data.is_valid():
            Category_data.save() 

    
    context = {'books':Book_data,
               'categories':Cat_data,
               'random_categories':Cat_random,
               'bookform':Book_form,
               'categoryform':Category_form,
               'allbooksnum':Book.objects.filter(active = True).count(),
               'availablebooksnum':Book.objects.filter(status = 'available').count(),
               'soldbooksnum':Book.objects.filter(status = 'sold').count(),
               'rentalbooksnum':Book.objects.filter(status = 'rental').count(),
               }
    return render(request,'pages/index.html',context)

def update(request, id, redirect_page = '/'):
    book_id = get_object_or_404(Book,id = id)
    if request.method == 'POST':
        book_update = BookForm(request.POST, request.FILES, instance = book_id)
        if book_update.is_valid():
            book_update.save()
            return redirect(redirect_page)
    else:
        book_update = BookForm(instance = book_id)
    context = {
        'updateform': book_update,
    }   
    return render(request, 'books/update.html', context)

def delete(request, id, redirect_page = '/'):
    book_delete = Book.objects.get(id = id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect(redirect_page)
        
    return render(request, 'books/delete.html')