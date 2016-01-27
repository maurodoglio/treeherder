# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import treeherder.model.fields


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0007_remove_datasource_oauth_fields'),
    ]

    operations = [
        # SQL: ALTER TABLE `failure_line` ADD COLUMN `best_classification_id` bigint NULL
        # migrations.AddField(
        #     model_name='failureline',
        #     name='best_classification',
        #     field=treeherder.model.fields.FlexibleForeignKey(related_name='best_for_lines', to='model.ClassifiedFailure', null=True),
        # ),
        migrations.AddField(
            model_name='failureline',
            name='best_is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='failurematch',
            name='classified_failure',
            field=treeherder.model.fields.FlexibleForeignKey(related_name='matches', to='model.ClassifiedFailure'),
        ),
        migrations.AlterIndexTogether(
            name='failureline',
            index_together=set([('job_guid', 'repository')]),
        ),
    ]
