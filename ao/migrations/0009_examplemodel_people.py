# Generated by Django 5.1.4 on 2025-01-01 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ao', '0008_rename_お名前_examplemodel_furigana_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='examplemodel',
            name='people',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
    ]
