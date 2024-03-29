# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-08-02 14:07
from __future__ import unicode_literals

import ckeditor_uploader.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manual', '0002_delete_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=256)),
                ('content', models.TextField(max_length=1000)),
                ('publish', models.DateTimeField()),
            ],
        ),
        migrations.AlterField(
            model_name='manual',
            name='context',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=' ', max_length=10000),
        ),
    ]
