# Generated by Django 3.2.25 on 2024-04-24 09:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0035_auto_20240424_0809'),
    ]

    operations = [
        migrations.RenameField(
            model_name='party',
            old_name='balance',
            new_name='current_balance',
        ),
    ]