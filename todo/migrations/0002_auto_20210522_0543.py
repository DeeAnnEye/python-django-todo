# Generated by Django 2.2.3 on 2021-05-22 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='task_time',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='task',
            name='task_date',
            field=models.CharField(max_length=200),
        ),
    ]