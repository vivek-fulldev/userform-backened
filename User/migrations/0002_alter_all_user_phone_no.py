# Generated by Django 3.2.3 on 2021-05-25 13:17

from django.db import migrations
import phone_field.models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='all_user',
            name='phone_no',
            field=phone_field.models.PhoneField(max_length=10),
        ),
    ]
