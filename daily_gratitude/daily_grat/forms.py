from django import forms

class GratForm(forms.Form):
    daily_entry = forms.CharField(label='I am thankful for:', max_length=10000)