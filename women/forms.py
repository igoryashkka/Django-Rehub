from django import forms
from .models import *
from django.core.exceptions import ValidationError


class AddPostForm(forms.ModelForm):
    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['cat'].empty_label = 'Not selected'
        
    class Meta:
        model = Women
        fields = ['title','slug','content','is_published','cat','photo']
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-input'}),
            'content': forms.Textarea(attrs={'cols':60,'rows':10}),
        }
  
    # user-validator : clean_nameoffiled(self)
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Title is too long')
        
        return title

  