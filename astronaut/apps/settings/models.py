from django.db import models


class WebParameter(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=9)
    site_description = models.TextField(max_length=400, null=True, blank=True)
    logo = models.ImageField(upload_to='dashboards/images', blank=True, null=True)
