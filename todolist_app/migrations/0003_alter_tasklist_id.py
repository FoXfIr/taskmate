# Generated by Django 4.1.7 on 2023-02-14 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todolist_app', '0002_tasklist_manage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasklist',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
