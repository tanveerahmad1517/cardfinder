# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-03-24 08:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LostCard', '0010_auto_20170206_1345'),
    ]

    operations = [
        migrations.RenameField(
            model_name='specs',
            old_name='Type',
            new_name='holder_name',
        ),
        migrations.RemoveField(
            model_name='card',
            name='HolderName',
        ),
        migrations.RemoveField(
            model_name='card',
            name='OrgName',
        ),
        migrations.RemoveField(
            model_name='card',
            name='PlaceLost',
        ),
        migrations.RemoveField(
            model_name='specs',
            name='favorite',
        ),
        migrations.RemoveField(
            model_name='specs',
            name='holder',
        ),
        migrations.AddField(
            model_name='specs',
            name='Org_Name',
            field=models.CharField(default='wee', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specs',
            name='id_card',
            field=models.CharField(default='2wh2', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='specs',
            name='phone_no',
            field=models.CharField(default='we2', max_length=20),
            preserve_default=False,
        ),
    ]
