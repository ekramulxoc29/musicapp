# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-14 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_song_fav'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='fav',
            field=models.BooleanField(default=False),
        ),
    ]
