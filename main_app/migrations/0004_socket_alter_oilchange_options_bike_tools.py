# Generated by Django 4.0.2 on 2022-04-13 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_remove_oilchange_filter_oilchange_filterchange'),
    ]

    operations = [
        migrations.CreateModel(
            name='Socket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.IntegerField()),
                ('drive', models.CharField(max_length=10)),
            ],
        ),
        migrations.AlterModelOptions(
            name='oilchange',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='bike',
            name='tools',
            field=models.ManyToManyField(to='main_app.Socket'),
        ),
    ]
