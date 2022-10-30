from django import forms

from main.models import Product, Shop, Category


class RandomForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок')
    content = forms.CharField(widget=forms.Textarea, label='Содержимое')


class ProductModelForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'category', 'shops']
