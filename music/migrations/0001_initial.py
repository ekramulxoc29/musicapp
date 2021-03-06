# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-10 23:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shilpi', models.CharField(max_length=200)),
                ('album_Name', models.CharField(max_length=200)),
                ('Genre', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Gaan_title', models.CharField(max_length=400)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='music.Album')),
            ],
        ),
    ]
