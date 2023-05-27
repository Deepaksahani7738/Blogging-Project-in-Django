from django import forms
from .models import BlogPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.forms import TextInput,Textarea,BooleanField


class PostBlogForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ('title','content')
        widget = {
            'title':forms.TextInput(attrs={
                'class':'form-control',
                'style':'max-width:300px',
                'placeholder':'Enter Blog Title'
            }),

            'content':forms.Textarea(attrs={
                'class':'form-control',
                'style':'max-width:400px'
            })
        }

class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','email','first_name','last_name','password1','password2']
        
    email = forms.EmailField(
        max_length=100,
        required=True,
        help_text='Enter Email Address',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Email'})
    )

    first_name = forms.CharField(
        max_length=100,
        required=True,
        help_text='Enter First Name',
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your First Name'})

    )

    last_name = forms.CharField(
    max_length=100,
    required=True,
    help_text='Enter Last Name',
    widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Your Last Name'})
    )

    username = forms.CharField(
        max_length=200,
        required=True,
        help_text= "Enter UserName",
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Enter UserName'})
    )

    password1 = forms.CharField(
        help_text='Enter Password',
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Enter Password'})
    )


    password2 = forms.CharField(
        help_text='Enter Password Again',
        required=True,
        widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'Confirm Password'})
    )

    check = forms.BooleanField(required=True)