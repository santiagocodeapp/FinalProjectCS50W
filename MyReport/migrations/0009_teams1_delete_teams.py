# Generated by Django 4.0.3 on 2022-03-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyReport', '0008_remove_players_team'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teams1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team_name', models.CharField(max_length=64)),
                ('team_head_coach', models.CharField(max_length=64)),
                ('team_pitching_coach', models.CharField(max_length=64)),
            ],
        ),
        migrations.DeleteModel(
            name='Teams',
        ),
    ]
