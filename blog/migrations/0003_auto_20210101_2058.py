# Generated by Django 3.1.4 on 2021-01-01 15:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_blogcomment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='Comment',
            new_name='comment',
        ),
    ]