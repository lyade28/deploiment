# Generated by Django 4.1.3 on 2022-11-11 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isep', '0002_alter_planning_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planning',
            name='date',
            field=models.CharField(max_length=200),
        ),
    ]
