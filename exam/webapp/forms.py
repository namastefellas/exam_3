from django import forms
from django.forms import widgets
from webapp.models import Product, Review

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'category', 'pic')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('product', 'description', 'score')



class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Search')