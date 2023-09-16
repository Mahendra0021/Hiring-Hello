from django import forms
from .models import CompanyModel



class Adduser(forms.ModelForm):

    model= CompanyModel
    fields='__all__'

    # Warning={
    #     'name':forms.TextInput(attrs={'class':'form-control'}),
    #         'Experience':forms.NumberInput(attrs={'class':'form-control'}),
    #         'position':forms.TextInput(attrs={'class':'form-control'})
    # }
