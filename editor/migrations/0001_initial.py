# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-01-31 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('article_heading', models.TextField()),
                ('article_head_lc_lang', models.TextField()),
                ('article', models.TextField()),
                ('group', models.CharField(max_length=255)),
                ('sub_grp', models.CharField(max_length=255)),
                ('publish_status', models.CharField(max_length=5)),
                ('proof_read_by', models.CharField(max_length=255)),
                ('content_dtp_person', models.CharField(max_length=255)),
                ('content_created_by', models.CharField(max_length=255)),
                ('image_name', models.CharField(max_length=255)),
                ('create_datetime', models.DateTimeField()),
                ('publish_datetime', models.DateTimeField()),
                ('will_expire', models.BooleanField(default=False)),
                ('expire_date', models.DateTimeField(default=None, null=True)),
            ],
        ),
    ]
