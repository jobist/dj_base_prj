# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20170704_2257'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'verbose_name_plural': 'Articles', 'verbose_name': 'Article'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories', 'verbose_name': 'Category'},
        ),
        migrations.AlterField(
            model_name='article',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Publication date'),
        ),
        migrations.AlterField(
            model_name='article',
            name='published',
            field=models.BooleanField(verbose_name='Published', default=True, db_index=True),
        ),
    ]
