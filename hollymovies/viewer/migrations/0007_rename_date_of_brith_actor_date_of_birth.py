# Generated by Django 4.0.6 on 2022-08-04 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0006_alter_movie_actors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='actor',
            old_name='date_of_brith',
            new_name='date_of_birth',
        ),
    ]
