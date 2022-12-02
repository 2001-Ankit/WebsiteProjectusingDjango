from django.shortcuts import render,redirect
from .models import *
from django.views.generic import View
from .views import *

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


from django.contrib.auth.models import User
from django.contrib import messages
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
