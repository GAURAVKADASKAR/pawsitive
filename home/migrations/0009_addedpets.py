# Generated by Django 5.1 on 2024-12-29 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_animalbehavior'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addedpets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveBigIntegerField()),
                ('Gender', models.CharField(max_length=20)),
                ('Diet', models.TextField()),
                ('AnimalPhoto', models.FileField(default='', upload_to='Animal_image')),
                ('mobilenumber', models.TextField()),
                ('Email', models.TextField()),
                ('Health_condition', models.TextField()),
                ('Allergies', models.TextField()),
                ('Breed', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.animalbreed')),
                ('animal_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.animal')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.registeration')),
                ('vaccination', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.vaccination')),
            ],
        ),
    ]
