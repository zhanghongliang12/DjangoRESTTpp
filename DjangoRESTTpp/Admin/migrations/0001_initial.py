# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdminUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('a_username', models.CharField(max_length=16, unique=True)),
                ('a_password', models.CharField(max_length=256)),
                ('is_delete', models.BooleanField(default=False)),
                ('is_super', models.BooleanField(default=False)),
            ],
        ),
    ]
