# Generated by Django 4.1.5 on 2023-03-15 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]