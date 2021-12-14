from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import *

class BookForm(forms.ModelForm):
    class Meta:
        model=Books
        fields=['title',
        'author',
        'photo_book',
        'photo_author',
        'pages',
        'price',
        'retal_price_day',
        'retal_peroid',
        'retal_total',
        'status',
        'category']

        widgets={'title':forms.TextInput(attrs={'class':'form-control'}),
        'author':forms.TextInput(attrs={'class':'form-control'}),
        'photo_book':forms.FileInput(attrs={'class':'form-control'}),
        'photo_author':forms.FileInput(attrs={'class':'form-control'}),
        'pages':forms.NumberInput(attrs={'class':'form-control'}),
        'price':forms.NumberInput(attrs={'class':'form-control'}),
        'retal_price_day':forms.NumberInput(attrs={'class':'form-control','id':'retal_price_day'}),
        'retal_peroid':forms.NumberInput(attrs={'class':'form-control','id':'retal_peroid'}),
        'retal_total':forms.NumberInput(attrs={'class':'form-control','id':'retal_total'}),
        'status':forms.Select(attrs={'class':'form-control'}),
        'category':forms.Select(attrs={'class':'form-control'})}
class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields=['name']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'})}

