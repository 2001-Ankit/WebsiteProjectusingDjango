from django.db import models


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


