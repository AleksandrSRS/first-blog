# Generated by Django 2.1.3 on 2018-11-19 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181118_0905'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Опрос', 'verbose_name_plural': 'Опросы'},
        ),
    ]
