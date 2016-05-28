# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('servicediscovery', '0002_auto_20160202_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='service',
            old_name='serviceName',
            new_name='service_name',
        ),
        migrations.RenameField(
            model_name='service_activiy',
            old_name='service_id',
            new_name='service',
        ),
        migrations.RemoveField(
            model_name='service_activiy',
            name='activiy_id',
        ),
    ]
