# Generated by Django 5.1.1 on 2024-12-06 10:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0004_alter_users_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCreditCart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomercart', models.BigIntegerField()),
                ('cvcode', models.BigIntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='first.users')),
            ],
        ),
    ]
