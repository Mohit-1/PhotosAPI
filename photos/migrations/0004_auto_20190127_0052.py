# Generated by Django 2.1.4 on 2019-01-26 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20190125_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='id',
        ),
        migrations.AddField(
            model_name='photo',
            name='pid',
            field=models.IntegerField(default=None, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
