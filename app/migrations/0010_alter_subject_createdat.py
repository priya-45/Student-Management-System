# Generated by Django 4.2.4 on 2023-11-02 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_subject'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]