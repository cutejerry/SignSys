# Generated by Django 2.2.1 on 2019-05-24 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SignModel', '0004_auto_20190524_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='name',
            field=models.CharField(max_length=64, verbose_name='已登记记录'),
        ),
    ]
