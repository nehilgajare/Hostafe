# Generated by Django 3.2.6 on 2021-11-28 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0008_hostelinfo_hostel_image_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hostelinfo',
            old_name='hostel_image_url',
            new_name='hostel_image_url_1',
        ),
        migrations.AddField(
            model_name='hostelinfo',
            name='hostel_image_url_2',
            field=models.URLField(blank=True, default=' ', null=True),
        ),
        migrations.AddField(
            model_name='hostelinfo',
            name='hostel_image_url_3',
            field=models.URLField(blank=True, default=' ', null=True),
        ),
    ]