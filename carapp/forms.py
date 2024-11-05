from django import forms
from .models import OrderVehicle

class OrderVehicleForm(forms.ModelForm):
    class Meta:
        model = OrderVehicle
        fields = ['vehicle', 'buyer', 'quantity']
        widgets = {
            'buyer': forms.Select(),  # Ensures a single selection for the buyer
        }
        labels = {
            'quantity': 'Vehicles Ordered',
        }

class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    subject = forms.CharField(max_length=150)
    message = forms.CharField(widget=forms.Textarea)
