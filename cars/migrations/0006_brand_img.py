# Generated by Django 4.2.3 on 2023-08-12 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0005_slide'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='img',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
