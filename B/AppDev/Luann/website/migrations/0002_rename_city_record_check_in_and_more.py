# Generated by Django 5.0.2 on 2024-04-01 03:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='record',
            old_name='city',
            new_name='check_in',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='state',
            new_name='check_out',
        ),
        migrations.RenameField(
            model_name='record',
            old_name='zipcode',
            new_name='payment_method',
        ),
    ]
