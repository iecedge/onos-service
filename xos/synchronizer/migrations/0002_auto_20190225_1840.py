# Copyright 2017-present Open Networking Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2019-02-25 23:40
from __future__ import unicode_literals

import core.models.xosbase_header
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onosapp_decl',
            name='app_id',
            field=core.models.xosbase_header.StrippedCharField(help_text=b'Application identifier', max_length=256),
        ),
        migrations.AlterField(
            model_name='onosapp_decl',
            name='dependencies',
            field=core.models.xosbase_header.StrippedCharField(blank=True, help_text=b'Comma separated list of required application application ids', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='onosapp_decl',
            name='url',
            field=core.models.xosbase_header.StrippedCharField(blank=True, help_text=b'URL at which the application is available, if it needs to be downloaded', max_length=1024, null=True),
        ),
        migrations.AlterField(
            model_name='onosapp_decl',
            name='version',
            field=core.models.xosbase_header.StrippedCharField(blank=True, help_text=b'Application version number', max_length=256, null=True),
        ),
        migrations.AlterField(
            model_name='onosservice_decl',
            name='rest_hostname',
            field=core.models.xosbase_header.StrippedCharField(help_text=b'Hostname of ONOS Service REST endpoint', max_length=255),
        ),
        migrations.AlterField(
            model_name='onosservice_decl',
            name='rest_password',
            field=core.models.xosbase_header.StrippedCharField(default=b'karaf', help_text=b'Password to use when authenticating to ONOS', max_length=255),
        ),
        migrations.AlterField(
            model_name='onosservice_decl',
            name='rest_port',
            field=models.IntegerField(default=8181, help_text=b'Port numnber of ONOS Service REST endpoint'),
        ),
        migrations.AlterField(
            model_name='onosservice_decl',
            name='rest_username',
            field=core.models.xosbase_header.StrippedCharField(default=b'karaf', help_text=b'Username to use when authenticating to ONOS', max_length=255),
        ),
    ]
