# Generated by Django 2.2.5 on 2019-12-29 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='likes',
            field=models.IntegerField(default=0, max_length=3),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.TextField(max_length=255),
        ),
    ]