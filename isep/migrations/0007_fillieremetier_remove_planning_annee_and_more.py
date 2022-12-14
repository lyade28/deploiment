# Generated by Django 4.1.3 on 2022-11-14 09:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('isep', '0006_alter_planning_annee'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilliereMetier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='planning',
            name='Annee',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='Semaine',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='heuredebut',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='heurefin',
        ),
        migrations.RemoveField(
            model_name='planning',
            name='salls',
        ),
        migrations.AddField(
            model_name='filiere',
            name='metier',
            field=models.CharField(choices=[('TIC', 'tic'), ('MA', 'ma')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='salle',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='isep.salle'),
        ),
        migrations.AlterField(
            model_name='cour',
            name='Libelle',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='filiere',
            name='Libelle',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='formateur',
            name='metiers',
            field=models.CharField(choices=[('TIC', 'tic'), ('MA', 'ma')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='formateur',
            name='name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='planning',
            name='activite',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='isep.cour'),
        ),
        migrations.AlterField(
            model_name='planning',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='planning',
            name='filiere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='isep.filiere'),
        ),
        migrations.AlterField(
            model_name='planning',
            name='formateur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='isep.formateur'),
        ),
        migrations.AlterField(
            model_name='planning',
            name='promo',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='salle',
            name='Libelle',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.CreateModel(
            name='Semaine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=200, null=True)),
                ('metier', models.CharField(choices=[('TIC', 'tic'), ('MA', 'ma')], max_length=200, null=True)),
                ('promo', models.CharField(max_length=200, null=True)),
                ('filiereMetiers', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='isep.fillieremetier')),
            ],
        ),
        migrations.AddField(
            model_name='fillieremetier',
            name='filiere',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='isep.filiere'),
        ),
        migrations.AddField(
            model_name='fillieremetier',
            name='planning',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='isep.planning'),
        ),
        migrations.AddField(
            model_name='planning',
            name='annee',
            field=models.CharField(max_length=300, null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='heureDebut',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='heureFin',
            field=models.TimeField(null=True),
        ),
        migrations.AddField(
            model_name='planning',
            name='semaine',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
