# Generated by Django 2.2.3 on 2019-08-12 08:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0003_auto_20190812_1353'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='scores',
            options={},
        ),
        migrations.RemoveField(
            model_name='scores',
            name='created',
        ),
    ]
