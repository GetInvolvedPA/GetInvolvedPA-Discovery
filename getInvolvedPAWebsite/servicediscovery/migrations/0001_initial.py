# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('service_id', models.IntegerField()),
                ('serviceName', models.TextField()),
                ('agency', models.TextField()),
                ('street', models.TextField()),
                ('city', models.TextField()),
                ('state', models.TextField()),
                ('zipcode', models.TextField()),
                ('country', models.TextField()),
                ('url', models.TextField()),
                ('contact_phone', models.TextField()),
                ('contact_name', models.TextField()),
                ('contact_email', models.TextField()),
                ('contact_address', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Service_Activiy',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activiy_id', models.IntegerField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('activiy_detail', models.TextField()),
                ('contact', models.TextField()),
                ('submitdate', models.DateField()),
                ('service_id', models.ForeignKey(to='servicediscovery.Service')),
            ],
        ),
        migrations.CreateModel(
            name='Service_Classification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('class_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('year_graduation', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='service_activiy',
            name='student',
            field=models.ForeignKey(to='servicediscovery.Student'),
        ),
        migrations.AddField(
            model_name='service',
            name='service_class_id',
            field=models.ForeignKey(to='servicediscovery.Service_Classification'),
        ),
    ]
