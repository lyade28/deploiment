from django.db import models
from isep.models import *

# Create your models here.

metier = [
    ("TIC", "tic"),
    ("MA", "ma"),

]


class Salle(models.Model):
    Libelle = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Libelle


class Filiere(models.Model):
    Libelle = models.CharField(max_length=300, null=True)
    metier = models.CharField(choices=metier, max_length=200, null=True)

    def __str__(self):
        return self.Libelle


class Cour(models.Model):
    Libelle = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.Libelle


class Formateur(models.Model):
    name = models.CharField(max_length=200, null=True)
    metiers = models.CharField(choices=metier, max_length=50, null=True)

    def __str__(self):
        return self.name


class Planning(models.Model):
    date = models.DateField(null=True)
    heureDebut = models.TimeField(null=True)
    heureFin = models.TimeField(null=True)
    activite = models.ForeignKey(Cour, on_delete=models.CASCADE, null=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, null=True)
    formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE, null=True)
    salle = models.ForeignKey(Salle, on_delete=models.CASCADE, null=True)
    promo = models.CharField(max_length=300, null=True)
    annee = models.CharField(max_length=300, null=True)
    semaine = models.CharField(max_length=300, null=True)

    def __str__(self):
        return self.promo


class FilliereMetier(models.Model):
    Libelle = models.CharField(max_length=300, null=True)
    metier = models.CharField(choices=metier, max_length=200, null=True)
    planning = models.ForeignKey(Planning, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.Libelle


class Semaine(models.Model):
    code = models.CharField(max_length=200, null=True)
    metier = models.CharField(choices=metier, max_length=200, null=True)
    promo = models.CharField(max_length=200, null=True)
    filiereMetiers = models.ForeignKey(FilliereMetier, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.promo
