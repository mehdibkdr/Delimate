from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from .models import User, Record, Deliverer
from django import forms

# - Register/Create a user

class CreateUserForm(UserCreationForm):

    full_name = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}))
    age = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Age', 'class': 'form-control'}))
    phone = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}))
    
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'full_name', 'age', 'phone']
    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None
        self.fields['full_name'].help_text = None
        self.fields['age'].help_text = None
        self.fields['phone'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None
        
    def save(self, commit=True):
        user = super(CreateUserForm, self).save(commit=False)
        user.full_name = self.cleaned_data['full_name']
        user.age = self.cleaned_data['age']
        user.phone = self.cleaned_data['phone']
        if commit:
            user.save()
        return user
        
# - Login a user

class LoginForm(AuthenticationForm):
    username = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}))
    password = forms.CharField(label='', widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'class': 'form-control'}))
    
# - Create a record

class CreateRecordForm(forms.ModelForm):
    
    delivery_man = forms.ModelChoiceField(
        queryset=Deliverer.objects.all(),
        empty_label='--Choose',
        label='',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Record
        fields = ['delivery_man', 'client_address', 'client_name', 'client_phone',  'price', 'status']

        labels = {
            'delivery_man': '',
            'client_address': '',
            'client_name': '',
            'client_phone': '',
            'price': '',
            'status': '',
        }

        widgets = {
            'delivery_man': forms.TextInput(attrs={'placeholder': 'Delivery Man', 'class': 'form-control'}),
            'client_address': forms.TextInput(attrs={'placeholder': 'Client Address', 'class': 'form-control'}),
            'client_name': forms.TextInput(attrs={'placeholder': 'Client Name', 'class': 'form-control'}),
            'client_phone': forms.TextInput(attrs={'placeholder': 'Client Phone', 'class': 'form-control'}),
            'price': forms.TextInput(attrs={'placeholder': 'Price', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        
        
# - Update a record

class UpdateRecordForm(forms.ModelForm):
    delivery_man = forms.ModelChoiceField(
        queryset=Deliverer.objects.all(),
        empty_label='--Choose',
        label='',
        widget=forms.Select(attrs={'class': 'form-control'})
    )
    
    class Meta:
        model = Record
        fields = ['delivery_man', 'client_address', 'client_name', 'client_phone',  'price', 'status']

        labels = {
            'delivery_man': '',
            'client_address': '',
            'client_name': '',
            'client_phone': '',
            'price': '',
            'status': '',
        }

        widgets = {
            'delivery_man': forms.TextInput(attrs={'placeholder': 'Delivery Man', 'class': 'form-control'}),
            'client_address': forms.TextInput(attrs={'placeholder': 'Client Address', 'class': 'form-control'}),
            'client_name': forms.TextInput(attrs={'placeholder': 'Client Name', 'class': 'form-control'}),
            'client_phone': forms.TextInput(attrs={'placeholder': 'Client Phone', 'class': 'form-control'}),
            'price': forms.TextInput(attrs={'placeholder': 'Price', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }
        
# - Create a deliverer

class CreateDelivererForm(forms.ModelForm):
    class Meta:
        model = Deliverer
        fields = ['full_name', 'age', 'address', 'phone_number']

        labels = {
            'full_name': '',
            'age': '',
            'address': '',
            'phone_number': '',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
            'age': forms.TextInput(attrs={'placeholder': 'Age', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
        }
        
        
# - Update a deliverer

class UpdateDelivererForm(forms.ModelForm):
    class Meta:
        model = Deliverer
        fields = ['full_name', 'age', 'address', 'phone_number']

        labels = {
            'full_name': '',
            'age': '',
            'address': '',
            'phone_number': '',
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'Full Name', 'class': 'form-control'}),
            'age': forms.TextInput(attrs={'placeholder': 'Age', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}),
        }