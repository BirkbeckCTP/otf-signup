# Generated by Django 3.1.1 on 2021-01-12 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0029_accesslogexportcode_organisation'),
    ]

    operations = [
        migrations.AddField(
            model_name='organisation',
            name='analytics_code',
            field=models.TextField(blank=True, help_text='Add all required JS here.', null=True),
        ),
    ]
