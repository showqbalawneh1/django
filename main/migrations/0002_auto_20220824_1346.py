# Generated by Django 3.1 on 2022-08-24 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorialContent',
            field=models.TextField(verbose_name='tutorialContent'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorialPublished',
            field=models.DateTimeField(verbose_name='date published'),
        ),
    ]
