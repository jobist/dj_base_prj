# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=128, unique=True, db_index=True)),
                ('slug', models.SlugField(max_length=128)),
                ('published', models.BooleanField(verbose_name='Опубликованно', db_index=True, default=True)),
                ('short_text', models.CharField(blank=True, null=True, max_length=255)),
                ('full_text', models.TextField()),
                ('created', models.DateTimeField(verbose_name='Создана', auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Статьи',
                'verbose_name': 'Статья',
                'db_table': 'article',
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=128, unique=True, db_index=True)),
                ('slug', models.SlugField(max_length=128)),
            ],
            options={
                'verbose_name': 'Категории',
                'db_table': 'category',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(to='blog.Category'),
        ),
    ]
