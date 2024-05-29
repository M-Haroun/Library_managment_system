from django.urls import path
from . import views

urlpatterns = [
    path('',views.books, name='books'),
    path('update/<int:id>',views.update_book, name='update'),
    path('delete/<int:id>',views.delete_book, name='delete'),
]