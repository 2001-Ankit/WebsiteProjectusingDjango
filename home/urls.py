from django.urls import path
from .views import *
urlpatterns =[
    path('', HomeView.as_view(), name='home'),
    path('categories/<slug>', Category, name='categories'),
    path('countries',Country, name='countries'),
    path('works', Works.as_view(),name='works'),
    path('signup', signup, name='signup'),
    path('aboutus',about,name='aboutus'),
    path('category',category,name='category'),
    path('product',product,name='product'),
    ]