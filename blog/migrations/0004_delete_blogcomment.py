# Generated by Django 3.1.4 on 2021-01-01 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20210101_2058'),
    ]

    operations = [
        migrations.DeleteModel(
            name='BlogComment',
        ),
    ]
