# Generated by Django 3.2.7 on 2021-09-15 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_profiles_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profiles',
            name='covid_vaccination_status',
            field=models.BooleanField(default=True),
        ),
    ]