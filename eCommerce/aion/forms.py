from django.contrib.auth.models import User
from .models import *
from django import forms
from django.contrib.auth import authenticate, login, logout, get_user_model

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ('username','password','email')

class UserDetailsForm(forms.ModelForm):
    
    class Meta:
        model = User_Details
        exclude = ('user_id','account_type', "billing_address", "shipping_address")
#        fields = ('username','password','first_name','last_name')

class AddressDetailsForm(forms.ModelForm):
    
    class Meta:
        model = Address_Details
        fields = '__all__'

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