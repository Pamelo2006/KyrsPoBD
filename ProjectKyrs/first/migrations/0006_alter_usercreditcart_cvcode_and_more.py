# Generated by Django 5.1.1 on 2024-12-06 11:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0005_usercreditcart'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='usercreditcart',
            name='cvcode',
            field=models.CharField(max_length=3),
        ),
        migrations.AlterField(
            model_name='usercreditcart',
            name='nomercart',
            field=models.CharField(max_length=16),
        ),
        migrations.AlterField(
            model_name='usercreditcart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]