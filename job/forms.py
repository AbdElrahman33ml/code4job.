from .models import Apply , job
from django import forms


class applyfrom(forms.ModelForm):
    
    class Meta:
        model = Apply
        fields = ['name','email','Portfolio_link','cv','cover_letter']


class jobform(forms.ModelForm):
    class Meta:
        model= job
        exclude = ['id','slug','owner']