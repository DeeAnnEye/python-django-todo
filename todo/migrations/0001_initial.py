# Generated by Django 2.2.3 on 2021-05-05 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_text', models.CharField(max_length=200)),
                ('task_date', models.DateTimeField(verbose_name='task date')),
            ],
        ),
    ]
