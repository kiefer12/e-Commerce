from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import generic
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
