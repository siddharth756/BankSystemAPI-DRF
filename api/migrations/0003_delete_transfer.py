# Generated by Django 5.1.2 on 2024-10-25 06:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_account_balance'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Transfer',
        ),
    ]
