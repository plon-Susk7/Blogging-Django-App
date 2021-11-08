from .models import addPost
from django.forms import ModelForm,Textarea

class Post(ModelForm):
    class Meta:
        model = addPost
        fields = ['title','description','body','image_url']

        widgets = {
            'body': Textarea(attrs={'cols': 80, 'rows': 5})
            }
