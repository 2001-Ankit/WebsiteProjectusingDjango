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
        self.context['products'] = Product.objects.all()
        return render(request, 'index.html', self.context)


class Works(BaseView):
    def get(self,request):
        self.context['answers'] = Work.objects.all()
        self.context['questions']= QnA.objects.all()

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
        self.context['products'] = Product.objects.filter(slug=slug)
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


class CartView(BaseView):

    def get(self,request):
        self.context
        username = request.user.username
        self.context['cart_views'] = Cart.objects.filter(username = username, checkout = False)
        return render(request,'cart.html',self.context)


def add_to_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(slug=slug, username=username, checkout=False).exists():
        quantity = Cart.objects.get(slug=slug, username=username,checkout=False).quantity
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price

        if discounted_price > 0:
            original_price = discounted_price
        else:
            original_price = price

        quantity = quantity + 1
        total = quantity * original_price
        Cart.objects.filter(slug = slug, username = username).update(quantity = quantity, total=total)
        return redirect('/')

    else:
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price

        if discounted_price > 0:
            original_price = discounted_price
        else:
            original_price = price
        data = Cart.objects.create(slug=slug,
                            username=username,
                            total=original_price,
                            items = Product.objects.filter(slug = slug)[0]
                            )

        data.save()
        return redirect('/')


def remove_cart(request,slug):
    username = request.user.username
    if Cart.objects.filter(slug=slug, username=username, checkout=False).exists():
        quantity = Cart.objects.get(slug=slug, username=username, checkout=False).quantity
        price = Product.objects.get(slug=slug).price
        discounted_price = Product.objects.get(slug=slug).discounted_price

        if discounted_price > 0:
            original_price = discounted_price
        else:
            original_price = price
        if quantity > 1:
            quantity = quantity - 1
        total = quantity * original_price
        Cart.objects.filter(slug=slug, username=username).update(quantity=quantity, total=total)
        return redirect('/')


def delete_cart(request,slug):
    username = request.user.username
    Cart.objects.filter(slug = slug, username=username ,checkout= False).delete()
    return redirect('/')


def wishlist(request,slug):
    if Product.objects.filter(slug=slug).exists():
        item = Product.objects.get(slug=slug)
        if not Wishlist.objects.filter(slug=slug,user=request.user).exists():

            price = item.price
            wishlist_object = Wishlist.objects.create(
                user=request.user,
                slug=slug,
                items = item,
                price = price,

            )
            wishlist_object.save()
            messages.success(request, f'{item.name} added to your wishlist')

        else:
            messages.info(request, f'{item.name} already added to your wishlist')

    else:
        messages.error(request, 'Selected Product Not Found')

    return redirect(request.META.get('HTTP_REFERER'))
