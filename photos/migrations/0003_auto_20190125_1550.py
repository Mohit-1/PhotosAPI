# Generated by Django 2.1.4 on 2019-01-25 10:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20181226_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='name',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
