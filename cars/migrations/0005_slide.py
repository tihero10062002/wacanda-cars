# Generated by Django 4.2.3 on 2023-08-01 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0004_testdrive'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='slide.jpg', upload_to='')),
            ],
        ),
    ]
