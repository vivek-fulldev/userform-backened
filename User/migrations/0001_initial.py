# Generated by Django 3.2.3 on 2021-05-25 13:15

from django.db import migrations, models
import phone_field.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='all_user',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_no', phone_field.models.PhoneField(max_length=31)),
            ],
            options={
                'verbose_name': 'User',
            },
        ),
    ]
