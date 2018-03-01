from django.shortcuts import render
from django.shortcuts import HttpResponse, render, redirect,HttpResponseRedirect, get_object_or_404, get_list_or_404
from django.views.generic import TemplateView
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


def login_view(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user= authenticate(username=username, password=password)
        login(request,user)
        return HttpResponseRedirect('/home/')
    return render(request, "aion/login.html",{"form":form, "title": title})
