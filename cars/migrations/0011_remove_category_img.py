# Generated by Django 4.2.3 on 2023-08-23 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0010_category_img'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='img',
        ),
    ]
