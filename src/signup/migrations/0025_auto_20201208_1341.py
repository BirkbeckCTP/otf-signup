# Generated by Django 3.1.1 on 2020-12-08 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0024_auto_20201208_1336'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='existing_customer',
            field=models.BooleanField(default=False, verbose_name='Customer in the last three years?'),
        ),
        migrations.AlterField(
            model_name='signup',
            name='phone_number',
            field=models.CharField(blank=True, help_text='Optional', max_length=200, null=True),
        ),
    ]
