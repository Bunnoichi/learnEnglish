# Generated by Django 3.2.25 on 2024-12-31 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordList', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='meaning',
            field=models.CharField(blank=True, max_length=200, verbose_name='意味'),
        ),
    ]
