# Generated by Django 5.1.1 on 2024-12-11 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0007_rename_nomercart_usercreditcart_nomer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usercreditcart',
            name='user',
        ),
    ]
