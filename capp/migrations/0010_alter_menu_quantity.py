# Generated by Django 3.2 on 2021-05-31 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capp', '0009_alter_menu_quantity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='quantity',
            field=models.IntegerField(null=True),
        ),
    ]
