# Generated by Django 4.2.3 on 2023-08-23 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0012_alter_testdrive_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(choices=[('1', 'красный'), ('2', 'зеленый'), ('3', 'синий'), ('4', 'белый'), ('5', 'черный'), ('6', 'серая')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='korobka',
            field=models.CharField(choices=[('Автоматическая', 'Автоматическая'), ('Механическая', 'Механическая')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='privod',
            field=models.CharField(choices=[('Передняя', 'Передний'), ('Задняя', 'задний'), ('Полная', 'полный')], max_length=255, null=True),
        ),
    ]
