# Generated by Django 3.2.4 on 2021-06-09 16:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('brightside', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='p_fname',
            new_name='p_first_name',
        ),
        migrations.RenameField(
            model_name='patient',
            old_name='p_lname',
            new_name='p_last_name',
        ),
    ]