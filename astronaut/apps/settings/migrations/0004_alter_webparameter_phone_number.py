# Generated by Django 4.1.4 on 2022-12-20 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('settings', '0003_webparameter_delete_post'),
    ]

    operations = [
        migrations.AlterField(
            model_name='webparameter',
            name='phone_number',
            field=models.TextField(max_length=9),
        ),
    ]
