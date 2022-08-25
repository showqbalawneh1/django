# Generated by Django 3.1 on 2022-08-25 15:59

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220824_1346'),
    ]

    operations = [
        migrations.CreateModel(
            name='tutorialCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categoryTutorial', models.CharField(max_length=200)),
                ('categorySummary', models.CharField(max_length=200)),
                ('categorySlug', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorialSlug',
            field=models.CharField(default=1, max_length=200),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='tutorialPublished',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 25, 15, 59, 5, 523732), verbose_name='date published'),
        ),
        migrations.CreateModel(
            name='tutorialSeries',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seriesTutorial', models.CharField(max_length=200)),
                ('seriesSummary', models.CharField(max_length=200)),
                ('categoryTutorial', models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.tutorialcategory')),
            ],
            options={
                'verbose_name_plural': 'Series',
            },
        ),
        migrations.AddField(
            model_name='tutorial',
            name='seriesTutorial',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.SET_DEFAULT, to='main.tutorialseries', verbose_name='Series'),
        ),
    ]
