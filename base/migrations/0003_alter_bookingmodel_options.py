# Generated by Django 4.2.2 on 2023-06-15 14:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_bookingmodel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bookingmodel',
            options={'permissions': [('create_booking', 'Can create booking'), ('change_booking', 'Can change booking'), ('delete_booking', 'Can delete booking'), ('get_booking', 'Can get booking')]},
        ),
    ]
