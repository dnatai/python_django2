# Generated by Django 4.2.5 on 2023-10-13 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weblog', '0005_post_draft_post_publish'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='draft',
            field=models.BooleanField(default=True),
        ),
    ]