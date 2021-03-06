# Generated by Django 3.1.1 on 2020-12-07 16:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0022_auto_20201203_1706'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessLogExportCode',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issued_to', models.CharField(max_length=255)),
                ('uuid', models.UUIDField(default=uuid.uuid4)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
    ]
