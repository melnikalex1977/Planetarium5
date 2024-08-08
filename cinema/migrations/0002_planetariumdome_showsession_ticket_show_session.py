# Generated by Django 5.0.7 on 2024-08-06 22:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanetariumDome',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('rows', models.IntegerField(default=0)),
                ('seats_in_row', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ShowSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('show_time', models.DateTimeField()),
                ('astronomy_show', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cinema.astronomyshow')),
                ('planetarium_dome', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cinema.planetariumdome')),
            ],
            options={
                'ordering': ['-show_time'],
            },
        ),
        migrations.AddField(
            model_name='ticket',
            name='show_session',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='cinema.showsession'),
            preserve_default=False,
        ),
    ]
