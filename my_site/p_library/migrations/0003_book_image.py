# Generated by Django 2.2.6 on 2020-04-27 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0002_auto_20200420_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, upload_to='book_images/%Y/%m/%d/'),
        ),
    ]
