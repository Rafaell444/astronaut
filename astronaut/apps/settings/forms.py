import re

from django import forms
from astronaut.apps.settings.models import WebParameter


class SiteParametersForm(forms.ModelForm):
    class Meta:
        model = WebParameter
        fields = ["title", "site_description", "email", "phone_number"]

    def clean(self):
        phone_number = self.cleaned_data['phone_number']
        email = self.cleaned_data['email']

        if not re.search(r'\b\d+\b', phone_number):
            raise forms.ValidationError('Please Provide Valid Number')

        if WebParameter.objects.filter(email=email).exists():
            raise forms.ValidationError('This Email Is Already Taken')