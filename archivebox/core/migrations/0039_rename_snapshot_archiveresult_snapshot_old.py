# Generated by Django 5.0.6 on 2024-08-18 06:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0038_rename_uuid_snapshot_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='archiveresult',
            old_name='snapshot',
            new_name='snapshot_old',
        ),
    ]
