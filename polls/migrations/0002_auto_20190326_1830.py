# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-03-26 18:30
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='client',
            old_name='address',
            new_name='password',
        ),
    ]