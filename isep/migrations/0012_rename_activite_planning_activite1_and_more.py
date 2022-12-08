# Generated by Django 4.1.3 on 2022-12-08 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('isep', '0011_alter_planning_activite_alter_planning_filiere_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='planning',
            old_name='activite',
            new_name='activite1',
        ),
        migrations.RenameField(
            model_name='planning',
            old_name='filiere',
            new_name='activite2',
        ),
        migrations.RenameField(
            model_name='planning',
            old_name='formateur',
            new_name='activite3',
        ),
        migrations.RenameField(
            model_name='planning',
            old_name='salle',
            new_name='formateur1',
        ),
        migrations.RenameField(
            model_name='planning',
            old_name='heureDebut',
            new_name='heureDebut1',
        ),
        migrations.RenameField(
            model_name='planning',
            old_name='heureFin',
            new_name='heureDebut2',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='annee',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='promo',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='semaine',
        ),
        migrations.AddField(
            model_name='planning',
            name='formateur2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='formateur3',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='heureDebut3',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='heureFin1',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='heureFin2',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='heureFin3',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='salle1',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='salle2',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='salle3',
            field=models.CharField(max_length=200, null=True),
        ),
    ]