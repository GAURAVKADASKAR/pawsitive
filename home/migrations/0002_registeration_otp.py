# Generated by Django 5.1 on 2024-12-29 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='registeration',
            name='otp',
            field=models.PositiveIntegerField(default=1),
            preserve_default=False,
        ),
    ]
