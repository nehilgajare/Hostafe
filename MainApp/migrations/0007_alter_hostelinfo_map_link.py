# Generated by Django 3.2.6 on 2021-11-17 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0006_alter_hostelinfo_map_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hostelinfo',
            name='map_link',
            field=models.CharField(default=' ', max_length=200, null=True),
        ),
    ]
