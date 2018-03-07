from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect,HttpResponseRedirect, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views import generic
from aion.forms import *
from django.contrib.auth import authenticate, login, logout, get_user_model
from .models import *

class HomePageView(TemplateView):
    template_name = 'home.html'
    
class HomeView(generic.ListView):
    template_name = 'aion/home.html'
    context_object_name = 'products'
#    paginate_by = 10
    queryset = Product.objects.all().order_by('-id')

#    def get_paginate_by(self, queryset):
#        self.paginate_by = self.request.GET.get('paginate_by', self.paginate_by)
#        return self.paginate_by
#    
#    def get_context_data(self, **kwargs):
#        context = super(HomeView, self).get_context_data(**kwargs)
#        context["loggeduser"] = self.request.user.id
#        context["offers"] = Offer.objects.filter(product_id__user_id = self.request.user.id).order_by('-id')
#        context["itemcount"] = self.request.GET.get('paginate_by', self.paginate_by)
#
#        return context

class UserFormView(generic.View):
    form_class = UserForm
    second_form_class = UserDetailsForm
    third_form_class = AddressDetailsForm
    title = "Register"
    template_name = 'aion/registration_form.html'
    
    #display blank form
    def get(self, request):
        form1 = self.form_class(None)
        form2 = self.second_form_class(None)
        form3 = self.third_form_class(None)
        return render(request, self.template_name,{'form1':form1,'form2':form2,'form3':form3, "title": self.title})
    
    #process form data
    def post(self, request):
        form1 = self.form_class(request.POST)
        form2 = self.second_form_class(request.POST)
        form3 = self.third_form_class(request.POST)
        
        if form1.is_valid() and form2.is_valid() and form3.is_valid():
            
            user = form1.save(commit=False)
            
            username = form1.cleaned_data['username']
            password = form1.cleaned_data['password']
            user.set_password(password)
            user.save()
            
            #return User objects if credentials are correct
            user = authenticate(username=username,password=password)
            
            if user is not None:
                
                if user.is_active:
                    login(request,user)
                    return HttpResponseRedirect('/home/')
                
        return render(request, self.template_name,{'form1':form1,'form2':form2,'form3':form3, "title": self.title})


def login_view(request):
	print(request.user)
	title = "Login"
	form = UserLoginForm(request.POST or None)
    
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user= authenticate(username=username, password=password)
		login(request,user)
		return HttpResponseRedirect('/home/')
	return render(request, "aion/login.html",{"form":form, "title": title})

class CreateProduct(CreateView):
	template_name = 'addproduct.html'
	model = Product
	fields = ['item_name','item_quantity','item_photo']

class ViewProduct(generic.DetailView):
    model = Product
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class ViewAccount(generic.DetailView):
    model = User
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_details"] = User_Details.objects.get(user_id=self.object)
        context["user"] = self.object
        
        return context

