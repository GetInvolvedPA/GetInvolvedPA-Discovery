# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicediscovery', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='service_class_id',
            new_name='service_classification',
        ),
        migrations.RemoveField(
            model_name='service',
            name='service_id',
        ),
    ]
