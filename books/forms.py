from django import forms
from .models import Book, Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        widgets = {
            'name' : forms.TextInput(attrs={'class': 'form-control'}),
        }
        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        exclude = ['active',]    # We put fields that we do not need them to appear in form
        
        widgets = {
            'title' : forms.TextInput(attrs={'class': 'form-control'}),
            'author' : forms.TextInput(attrs={'class': 'form-control'}),
            'photo_book' : forms.FileInput(attrs={'class': 'form-control'}),
            'photo_author' : forms.FileInput(attrs={'class': 'form-control'}),
            'pages' : forms.NumberInput(attrs={'class': 'form-control'}),
            'price' : forms.NumberInput(attrs={'step': 0.01,'class': 'form-control', 'id':'bookPrice'}),
            'profit_ratio' : forms.NumberInput(attrs={'step': 0.01,'class': 'form-control', 'id':'profitratio'}),
            'profits' : forms.NumberInput(attrs={'step': 0.01,'class': 'form-control', 'id':'allprofits'}),
            'retal_price_day' : forms.NumberInput(attrs={'step': 0.01,'class': 'form-control', 'id':'retalDayPrice'}),
            'retal_period' : forms.NumberInput(attrs={'class': 'form-control','id':'retalDays'}),
            'retal_total' : forms.NumberInput(attrs={'class': 'form-control', 'id':'retalTotal'}),
            'status' : forms.Select(attrs={'class': 'form-control'}),
            'category' : forms.Select(attrs={'class': 'form-control'}),          
        }
        
