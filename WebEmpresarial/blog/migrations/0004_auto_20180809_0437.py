# Generated by Django 2.1 on 2018-08-09 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180809_0245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(related_name='get_post', to='blog.Categoria', verbose_name='Categorias'),
        ),
    ]
