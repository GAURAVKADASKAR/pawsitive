# Generated by Django 5.1 on 2024-12-29 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_registeration_isactive'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registeration',
            old_name='isActive',
            new_name='is_Active',
        ),
    ]
