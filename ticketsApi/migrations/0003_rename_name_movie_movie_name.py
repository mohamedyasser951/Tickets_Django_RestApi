# Generated by Django 4.2.3 on 2023-07-30 03:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ticketsApi', '0002_remove_movie_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='name',
            new_name='movie_name',
        ),
    ]
