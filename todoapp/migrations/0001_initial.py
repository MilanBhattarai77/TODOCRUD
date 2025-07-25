# Generated by Django 5.2.4 on 2025-07-04 05:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('address', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.TimeField(auto_created=True)),
                ('title', models.CharField()),
                ('completed', models.BooleanField(default=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='todoapp.customer')),
            ],
        ),
    ]
