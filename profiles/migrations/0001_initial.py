# Generated by Django 3.2.7 on 2021-09-11 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('photo', models.CharField(max_length=5000)),
                ('bio', models.CharField(max_length=500)),
                ('job_title', models.CharField(blank=True, max_length=100)),
                ('company', models.CharField(blank=True, max_length=100)),
                ('school', models.CharField(blank=True, max_length=100)),
                ('covid_vaccination_status', models.BooleanField(blank=True, default=True)),
                ('current_city', models.CharField(max_length=50)),
                ('hometown', models.CharField(max_length=50)),
                ('gender', models.CharField(max_length=100)),
                ('sexual_orientation', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('astrological_sign', models.CharField(max_length=100)),
                ('interests_hobbies', models.CharField(max_length=100)),
                ('favorite_restaurant', models.CharField(max_length=100)),
                ('favorite_bar', models.CharField(max_length=100)),
                ('religion', models.CharField(max_length=100)),
                ('drinking', models.CharField(max_length=100)),
                ('smoking', models.CharField(max_length=100)),
                ('kids', models.CharField(max_length=100)),
                ('politics', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
