from django import forms
from django.forms import ModelForm, widgets
from .models import Trip
from django import forms
from django.core.files.uploadedfile import SimpleUploadedFile




class TripForm(forms.ModelForm):
    # city = forms.TextInput()
    # country = forms.TimeField()
    # continent = forms.ModelChoiceField(queryset= Continent.objects.all())
    # description = forms.Textarea()
    # photo = forms.ImageField()
    
    class Meta:
        model = Trip
        fields = ('city', 'country', 'continent', 'description', 'photo')

        widget = {
            'city': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs ={'class': 'form-control'}),
            'continents': forms.SelectMultiple(attrs= {'class':'form-control'}),
            'description': forms.TextInput(attrs = {'class': 'form-control'}),
            # 'photo': forms.ImageField(attrs = {'class': 'form-control'}),
        }