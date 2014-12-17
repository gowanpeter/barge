# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('heart', '0002_auto_20141217_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='piece',
            name='exhibition',
            field=models.ForeignKey(to='heart.Exhibition', default='boola'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='piece',
            name='publication',
            field=models.ForeignKey(to='heart.Publication', default='boolee'),
            preserve_default=False,
        ),
    ]
