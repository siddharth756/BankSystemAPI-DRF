# Generated by Django 5.1.2 on 2024-10-25 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_name_bank_bank_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branch',
            old_name='address',
            new_name='branch_address',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='address',
            new_name='customer_address',
        ),
        migrations.RenameField(
            model_name='customer',
            old_name='phone',
            new_name='customer_phone',
        ),
    ]
