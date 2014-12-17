# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConditionChoice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('condition', models.CharField(max_length=1, choices=[('a', 'Pristine'), ('b', 'Used, good'), ('c', 'Used, worn'), ('d', 'Cracked / chipped'), ('e', 'Broken')])),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Exhibition',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('exhibition_name', models.CharField(max_length=45, default='', blank=True)),
                ('exhibition_date', models.DateField(null=True, blank=True)),
                ('exhibition_description', models.CharField(max_length=1000, default='', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('publication_name', models.CharField(max_length=45, default='', blank=True)),
                ('publication_date', models.DateField(null=True, blank=True)),
                ('publication_author', models.CharField(max_length=45, default='', blank=True)),
                ('publication_media', models.CharField(max_length=45, default='', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='piece',
            name='catalogue_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='cataloguer',
            field=models.CharField(max_length=45, default='', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='condition',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='height_inches',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='height_mm',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='length_inches',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='length_mm',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='weight_grams',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='weight_ounces',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='width_inches',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='piece',
            name='width_mm',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
