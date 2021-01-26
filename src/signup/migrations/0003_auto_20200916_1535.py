# Generated by Django 3.1.1 on 2020-09-16 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0002_package_front_page'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organisation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the organisation running this site.', max_length=300)),
                ('address_one', models.CharField(max_length=300)),
                ('address_two', models.CharField(max_length=300)),
                ('post_code', models.CharField(help_text='Post or Zip Code', max_length=20)),
                ('main_page_hero_text', models.CharField(help_text='Hero text that appears on the home page directly under the nav bar.', max_length=300, null=True)),
                ('hero_card_one_title', models.CharField(max_length=300, null=True)),
                ('hero_card_one_text', models.TextField(null=True)),
                ('hero_card_one_image', models.ImageField(upload_to='')),
                ('hero_card_two_title', models.CharField(max_length=300, null=True)),
                ('hero_card_two_text', models.TextField(null=True)),
                ('hero_card_two_image', models.ImageField(upload_to='')),
                ('hero_card_three_title', models.CharField(max_length=300, null=True)),
                ('hero_card_three_text', models.TextField(null=True)),
                ('hero_card_three_image', models.ImageField(upload_to='')),
                ('copyright_notice', models.CharField(help_text='Appears in the footer below links and such', max_length=300, null=True)),
                ('contact_email', models.EmailField(help_text='This email address will be used for the contact form.', max_length=254, null=True)),
                ('twitter_url', models.URLField(help_text='Enter the full account url eg. https://twitter.com/openlibhums', max_length=100, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='package',
            name='items',
            field=models.TextField(help_text='Items available in this package. We recommend using a orderedor unordered list.', null=True),
        ),
    ]
