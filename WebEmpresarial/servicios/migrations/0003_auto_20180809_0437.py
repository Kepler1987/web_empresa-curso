# Generated by Django 2.1 on 2018-08-09 09:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('servicios', '0002_auto_20180809_0242'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='servicio',
            options={'ordering': ['created'], 'verbose_name': 'servicio', 'verbose_name_plural': 'servicios'},
        ),
    ]
