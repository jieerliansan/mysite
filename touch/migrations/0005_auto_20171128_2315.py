# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-28 15:15
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('touch', '0004_question'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='artilce',
            new_name='article',
        ),
    ]
