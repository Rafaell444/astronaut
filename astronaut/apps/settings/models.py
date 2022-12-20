from django.db import models


class Webpara(models.Model):
    title = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(max_length=400,null=True,blank=True)
    logo = models.ImageField(upload_to='dashboards/images', blank=True, null=True,)

