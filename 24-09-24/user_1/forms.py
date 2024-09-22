from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'class': 'form-control',  # Adding the class
        'placeholder': 'Email'
    }))
    
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',  # Adding the class
        'placeholder': 'Username'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',  # Adding the class
        'placeholder': 'Password'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',  # Adding the class
        'placeholder': 'Confirm Password'
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


from django import forms
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_pic', 'country', 'company_name', 'industry', 'hourly_rate', 'experience', 'skills', 'languages', 'about']
        widgets = {
            'profile_pic': forms.FileInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'industry': forms.TextInput(attrs={'class': 'form-control'}),
            'hourly_rate': forms.NumberInput(attrs={'class': 'form-control'}),
            'experience': forms.Textarea(attrs={'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'class': 'form-control'}),
            'languages': forms.Textarea(attrs={'class': 'form-control'}),
            'about': forms.Textarea(attrs={'class': 'form-control'}),
        }





# ***************************************************************************************

from django import forms
from .models import ImagePost

class ImagePostForm(forms.ModelForm):
    class Meta:
        model = ImagePost
        fields = ['title', 'image', 'description']

# *********************************************************************

from .models import JobPost
from django import forms
from .models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = ['job_title', 'skills', 'duration', 'category', 'experience', 'budget', 'description']

    def __init__(self, *args, **kwargs):
        super(JobPostForm, self).__init__(*args, **kwargs)
        self.fields['job_title'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter job title'})
        self.fields['skills'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter required skills'})
        self.fields['duration'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter job duration'})
        self.fields['category'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Select category'})
        self.fields['experience'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter required experience'})
        self.fields['budget'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter budget'})
        self.fields['description'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Provide job description', 'rows': 3})



