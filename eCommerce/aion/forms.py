from django.contrib.auth.models import User
from .models import *
from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model

#class UserForm(forms.ModelForm):
#    password = forms.CharField(widget=forms.PasswordInput)
#    
#    class Meta:
#        model = User
#        fields = ('username','password','first_name','last_name')
#        labels = {
#            'first_name': 'Name',
#            'last_name': 'Degree Program/Office'
#        }
#
#class OfferPurchaseForm(forms.ModelForm):
#    class Meta:
#        model = Offer
#        fields = ('purchase_offer',)
#        #exclude = ('user_id','post_id','isAccept','reason','isPurchase')
#    
#    def __init__(self, *args, **kwargs):
#        self.user = kwargs.pop('user')
#        super(OfferPurchaseForm, self).__init__(*args, **kwargs)
#        #self.fields['exchange_offer'].queryset = Post.objects.filter(user_id__id=self.user.id)
#        
#class OfferExchangeForm(forms.ModelForm):
#    class Meta:
#        model = Offer
#        fields = ('exchange_offer',)
#        #exclude = ('user_id','post_id','isAccept','reason','isPurchase')
#    
#    def __init__(self, *args, **kwargs):
#        self.user = kwargs.pop('user')
#        super(OfferExchangeForm, self).__init__(*args, **kwargs)
#        self.fields['exchange_offer'].queryset = Post.objects.filter(user_id__id=self.user.id)
#
#        
class UserLoginForm(forms.Form):
    User = get_user_model()
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self, *args, **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = authenticate(username=username, password=password)

        
        #user = User.objects.filter(username=username)
        #if user_qs.count()==1:
        #    user = user_qs.first()
        if username and password:
            user = authenticate(username=username, password= password)
            if not user:
                raise forms.ValidationError("Incorrect Username or Password")
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Username or Password")
                
        return super(UserLoginForm, self).clean(*args, **kwargs)