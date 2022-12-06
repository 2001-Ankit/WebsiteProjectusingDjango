from django.db import models
from django.contrib.auth.models import User
from .

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media')
    slug = models.CharField(max_length=400)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=400)
    slug = models.CharField(max_length=400)
    image = models.ImageField(upload_to='media')
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    specification = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Country(models.Model):
    cname = models.CharField(max_length=40)
    logo = models.CharField(max_length=300)

    def __str__(self):
        return self.cname


class Work(models.Model):
    name = models.CharField(max_length=800)

    def __str__(self):
        return self.name


class QnA(models.Model):
    name = models.CharField(max_length=400)
    question = models.CharField(max_length=900)
    answer = models.CharField(max_length=900)

    def __str__(self):
        return self.name

class Wishlist(models.Model):
user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)# here CASCADE is the behavior to adopt when the referenced object(because it is a foreign key) is deleted. it is not specific to django,this is an sql standard.
wished_item = models.ForeignKey(Item,on_delete=models.CASCADE)
slug = models.CharField(max_length=30,null=True,blank=True)
added_date = models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.wished_item.title