from django import forms
from .models import Advertisement
from django.core.exceptions import ValidationError


def question(title):
    if title[0] == '?':
        raise ValidationError('Заголовок не может начинаться с "?"')


def not_negative(price):
    if price < 1:
        raise ValidationError('Цена не может быть ниже 1')


class AdvertisementForm(forms.ModelForm):
    title = forms.CharField(validators=[question],
                            max_length=64,
                            widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    description = forms.CharField(required=False,
                                  widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
    price = forms.DecimalField(validators=[not_negative],
                               widget=forms.NumberInput(attrs={'class': 'form-control form-control-lg'}))
    auction = forms.BooleanField(required=False,
                                 widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    image = forms.ImageField(required=False,
                             widget=forms.FileInput(attrs={'class': 'form-control form-control-lg'}))

    class Meta:
        model = Advertisement
        fields = ['title', 'description', 'price', 'auction', 'image']
        widgets = {'title': forms.TextInput(attrs={'class': 'form-control form-control-lg'}),
                   'description': forms.Textarea(attrs={'class': 'form-control form-control-lg'},),
                   'price': forms.NumberInput(attrs={'class': 'form-control form-control-lg'}),
                   'auction': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
                   'image': forms.FileInput(attrs={'class': 'form-control form-control-lg'})
                   }
