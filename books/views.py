from django.shortcuts import render
from .models import Book, Category
from .forms import CategoryForm
from pages.views import update,delete
from django.db.models import Q

# Create your views here.
def books(request):
    search=Book.objects.all()
    Cat_data=Category.objects.all()
    Category_form=CategoryForm()
    input_value = None
    
    if 'search_name' in request.GET:
        input_value = request.GET['search_name']
        if input_value:
            # Check the input values are the numeric or string
            # if numeric search in prices else serch in title or auther names
            try:
                price = float(input_value)
                search = search.filter(
                    Q(price__lte = price)|Q(retal_price_day__lte = price))
            except ValueError:
                # Use Q objects to combine filters
                search = search.filter( 
                                   Q(title__icontains = input_value) | Q(author__icontains = input_value)
                                   )
    
    
    if request.method == 'POST':      
        Category_data = CategoryForm(request.POST)
        if Category_data.is_valid():
            Category_data.save()
             
    context = {'books':search,
               'categories':Cat_data,
               'categoryform':Category_form,
               }
    return render(request,"books/books.html",context)

def update_book(request, id):
    return update(request, id,'books')

def delete_book(request, id):
    return delete(request, id,'books')
    