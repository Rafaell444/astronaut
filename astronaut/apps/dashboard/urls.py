from django.urls import path

from astronaut.apps.dashboard.views import dashboard
from astronaut.apps.settings.views import SiteParametersView

urlpatterns = [

    path("dashboard/", dashboard, name="dashboard"),
    path("dashboard/settings", SiteParametersView.as_view(), name="WebsiteSettings"),

]
