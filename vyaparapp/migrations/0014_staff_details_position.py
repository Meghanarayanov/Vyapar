# Generated by Django 4.2.3 on 2023-11-22 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vyaparapp', '0013_deleteddeliverychallan_deletedestimate_deliverychallan_deliverychallanitems_deliverychallantransacti'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff_details',
            name='position',
            field=models.CharField(blank=True, default='staff', max_length=255, null=True),
        ),
    ]