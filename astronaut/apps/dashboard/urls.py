from django.urls import path
from . import views

urlpatterns = [
	
	path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/settings", views.WebsiteSettings, name="WebsiteSettings"),

]