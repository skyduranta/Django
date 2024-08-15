from django import forms
from .models import SkyColor


class SkyColorForm(forms.Form):
    sky_variety = forms.ModelChoiceField(
        queryset=SkyColor.objects.all(), label="Select Sky Color"
    )
