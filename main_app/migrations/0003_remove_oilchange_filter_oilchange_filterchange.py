# Generated by Django 4.0.2 on 2022-04-13 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_oilchange'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='oilchange',
            name='filter',
        ),
        migrations.AddField(
            model_name='oilchange',
            name='filterChange',
            field=models.BooleanField(default=False, verbose_name='Oil Filter Change'),
        ),
    ]