# Generated by Django 5.1.4 on 2025-01-02 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ao', '0013_alter_examplemodel_check_in_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examplemodel',
            name='check_in_date',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='examplemodel',
            name='check_out_date',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
    ]
