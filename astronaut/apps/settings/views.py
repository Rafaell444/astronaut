from django.shortcuts import render
from django.views import View

from astronaut.apps.settings.models import WebParameter
from astronaut.apps.settings.forms import SiteParametersForm


class SiteParametersView(View):
    def get(self, request, *args, **kwargs):
        site_settings_form = SiteParametersForm()
        return render(request, "dashboard/pages/websettings.html", {'site_settings_form': site_settings_form})

    def post(self, request, *args, **kwargs):
        site_settings_form = SiteParametersForm(request.POST)
        if site_settings_form.is_valid():
            site_settings_form.save()
            return render(request, "dashboard/pages/websettings.html", {'site_settings_form': site_settings_form})
        else:
            return render(request, "dashboard/pages/websettings.html", {'site_settings_form': site_settings_form})
