# Generated by Django 4.2.7 on 2023-12-31 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
    ]
