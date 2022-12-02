from django.urls import path
from .views import *
from .models import *
urlpatterns =[
    path('', HomeView.as_view(), name='home'),
    path('categories/<slug>', Category, name='categories'),
    path('countries',Country, name='countries'),
    path('works', Works.as_view(),name='works'),
    path('signup', signup, name='signup'),
    ]