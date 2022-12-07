from django.db import models
from django.contrib.auth.models import User


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

class Cart(models.Model):
    username = models.CharField(max_length=400)
    slug = models.CharField(max_length=500)
    items = models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    total = models.IntegerField()
    checkout = models.BooleanField(default=False)

    def __str__(self):
        return self.username


class Wishlist(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    items = models.ForeignKey(Product, on_delete = models.CASCADE)
    slug = models.CharField(max_length = 400)
    price = models.IntegerField()

    def __str__(self):
        return f"< {self.user.username}  : {self.items.name} >"

