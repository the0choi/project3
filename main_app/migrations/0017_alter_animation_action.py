# Generated by Django 4.2.4 on 2023-08-24 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20230824_0422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='animation',
            name='action',
            field=models.CharField(choices=[('Move', 'Move'), ('Kick', 'Kick'), ('Dance', 'Dance'), ('Jump', 'Jump')], max_length=20),
        ),
    ]
