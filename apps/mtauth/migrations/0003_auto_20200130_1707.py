# Generated by Django 2.2.9 on 2020-01-30 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mtauth', '0002_auto_20200128_2329'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mtuser',
            old_name='uid',
            new_name='id',
        ),
    ]