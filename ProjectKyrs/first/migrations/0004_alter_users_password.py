# Generated by Django 5.1.1 on 2024-12-01 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0003_remove_users_cv_doce_remove_users_nomer_cart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='password',
            field=models.CharField(max_length=10),
        ),
    ]