# Generated by Django 4.2.2 on 2023-06-15 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_addressmodel_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pitchmodel',
            name='imgs',
            field=models.ManyToManyField(blank=True, default=None, null=True, to='base.mediamodel'),
        ),
    ]
