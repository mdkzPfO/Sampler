# Generated by Django 3.2.12 on 2022-04-03 08:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exp1app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animalmodel',
            old_name='Animal',
            new_name='animal',
        ),
        migrations.RenameField(
            model_name='animalmodel',
            old_name='purpose',
            new_name='animal_purpose',
        ),
    ]
