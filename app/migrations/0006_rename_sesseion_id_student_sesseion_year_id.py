# Generated by Django 4.2.4 on 2023-10-18 08:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_rename_sesseoin_id_student_sesseion_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='sesseion_id',
            new_name='sesseion_year_id',
        ),
    ]