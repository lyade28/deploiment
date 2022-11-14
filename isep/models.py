from django.db import models
from isep.models import *

# Create your models here.

metier = [
    ("TIC", "tic"),
    ("MA", "ma"),

]


class Salle(models.Model):
    libelle = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.libelle


class Filiere(models.Model):
    libelle = models.CharField(max_length=300, null=True)
    metier = models.CharField(choices=metier, max_length=200, null=True)

    def __str__(self):
        return self.libelle


class Cour(models.Model):
    libelle = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.libelle


class Formateur(models.Model):
    name = models.CharField(max_length=200, null=True)
    metiers = models.CharField(choices=metier, max_length=50, null=True)

    def __str__(self):
        return self.name


class Planning(models.Model):
    date = models.DateField(null=True)
    heureDebut = models.TimeField(null=True)
    heureFin = models.TimeField(null=True)
    activite = models.CharField(  max_length=200, null=True)
    filiere = models.CharField( max_length=200, null=True)
    formateur = models.CharField( max_length=200, null=True)
    salle = models.CharField( max_length=200, null=True)
    promo = models.CharField(max_length=300, null=True)
    annee = models.CharField(max_length=300, null=True)
    semaine = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.promo


class FilliereMetier(models.Model):
    libelle = models.CharField(max_length=300, null=True)
    metier = models.CharField(choices=metier, max_length=200, null=True)
    planning = models.ManyToManyField(Planning)

    def __str__(self):
        return self.libelle


class Semaine(models.Model):
    code = models.CharField(max_length=200, null=True)
    metier = models.CharField(choices=metier, max_length=200, null=True)
    promo = models.CharField(max_length=200, null=True)
    filiereMetier = models.ManyToManyField(FilliereMetier)

    def __str__(self):
        return self.promo
