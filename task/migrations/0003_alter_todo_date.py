# Generated by Django 4.0.6 on 2022-07-18 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_alter_todo_due_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
