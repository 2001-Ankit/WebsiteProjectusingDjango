from django.shortcuts import render,redirect
from .models import *
from django.views.generic import View
from .views import *
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


class BaseView(View):
    context={}


class HomeView(BaseView):
    def get(self,request):
        self.context['categories'] = Category.objects.all()
        self.context['countries'] = Country.objects.all()

        return render(request, 'index.html', self.context)


class Works(BaseView):
    def get(self,request):
        self.context['answers'] = Work.objects.all()

        return render(request,'howitworks.html',self.context)



class Categories(BaseView):
    def get(self, request, slug):
        self.context
        ids = Category.objects.get(slug=slug).id
        self.context['category'] = Product.objects.filter(category_id=ids)
        return render(request, 'category.html', self.context)

class Products(BaseView):
    def get(self,request,slug):
        self.context
        self.context['products'] = Product.objects.filter(slug = slug)
        return render(request, 'productpage.html', self.context)

def signup(request):
    if request.method == 'POST':
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cpassword =request.POST['cpassword']
        if password == cpassword:
            if User.objects.filter(username = username).exists():
                messages.error(request,"The user name is already taken")
                return redirect('/signup')
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email already used")
            else:
               user =  User.objects.create_user(
                   username = username,
                   email = email,
                   password = password
               )
               user.save()
        else:
            messages.error(request,"Password doesnot match")
            return redirect('/signup')



    return render(request,'signup.html')


class SearchView(BaseView):
    def get(self,request):
        query = request.GET.get('query')
        if not query:
            return redirect('/')
        self.context['search_product'] = Product.objects.filter(name__icontains = query)
        return render(request,'search.html',self.context)


def about(request):
    if request.method == 'POST':
        email = request.POST['email']
    return render(request,'about-us.html')




