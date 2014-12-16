# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Piece',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('catalogue_id', models.CharField(max_length=45)),
                ('heath_id', models.CharField(blank=True, max_length=45)),
                ('piece_name', models.CharField(blank=True, max_length=45)),
                ('piece_description', models.CharField(blank=True, max_length=2000)),
                ('manufactured_date', models.DateField(blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
