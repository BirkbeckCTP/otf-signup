# Generated by Django 3.1.1 on 2020-11-09 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0016_resource'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organisation',
            old_name='faq',
            new_name='FAQ',
        ),
    ]
