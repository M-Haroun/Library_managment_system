from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=250)
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    status_Book=[
        ('available','available'),
        ('rental','rental'),
        ('sold','sold')
    ]
    title = models.CharField(max_length=250)
    auther = models.CharField(max_length=250, null=True,  blank=True)
    photo_book = models.ImageField(upload_to='photos/book/%y/%m/%d', null=True,  blank=True)
    photo_auther= models.ImageField(upload_to='photos/auther/%y/%m/%d', null=True,  blank=True)
    pages = models.IntegerField(null=True,  blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2,null=True,  blank=True)
    retal_price_day = models.DecimalField(max_digits=8, decimal_places=2,null=True,  blank=True)
    retal_period = models.IntegerField(null=True,  blank=True)
    active = models.BooleanField(default= True)
    status = models.CharField(max_length=50, null=True,  blank=True, choices= status_Book)
    category = models.ForeignKey(Category, on_delete=models.PROTECT,null=True,  blank=True)
    
    
    def __str__(self):
        return self.title