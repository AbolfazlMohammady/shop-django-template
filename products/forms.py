from django import forms

from .models import Product, Comment


class ProductForms(forms.ModelForm):
    class Meta:
        model= Product
        fields= ('title', 'description', 'price', 'active', )
        

class CommentForm(forms.ModelForm):
    class Meta:
        model= Comment
        fields= ('body', 'stars',)


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'short_description', 'price', 'active', 'image', 'size', 'weight', 'category', 'color', 'discount']
