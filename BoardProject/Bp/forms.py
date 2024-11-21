from django import forms
from .models import Boardgame, Description

class BoardgameForm(forms.ModelForm):
    class Meta:
        model = Boardgame
        fields = ['title', 'total_copies', 'available_copies']

#class DescriptionForm(forms.ModelForm):
    #class Meta:
       # model = Description
       # fields = ['title','description']
      #  widgets = {'description': forms.Textarea(attrs={'cols': 80})}
class DescriptionForm(forms.ModelForm):
    class Meta:
        model = Description
        fields = ['description']  # Only allow editing the description text
        widgets = {
            'description': forms.Textarea(attrs={'cols': 80}),
        }

