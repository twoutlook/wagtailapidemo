# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('demo', '0002_auto_20150917_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogindexpage',
            name='exclude_from_api',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='blogpage',
            name='exclude_from_api',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='contactpage',
            name='exclude_from_api',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventindexpage',
            name='exclude_from_api',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='eventpage',
            name='exclude_from_api',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='homepage',
            name='exclude_from_api',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='personpage',
            name='exclude_from_api',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='standardindexpage',
            name='exclude_from_api',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='standardpage',
            name='exclude_from_api',
            field=models.BooleanField(default=False),
        ),
    ]
