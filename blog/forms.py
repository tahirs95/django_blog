from django import forms
from .models import Article
 
 
class ArticleForm(forms.ModelForm):
    image = forms.ImageField()

 
    class Meta:
        model = Article
 
        fields = [
            "title",
            "tags",
            "image",
            "content",
        ]
