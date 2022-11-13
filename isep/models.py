from django.db import models
from .models import *


# Create your models here.

class Salle(models.Model):
    Libelle = models.CharField(max_length=200)

    def __str__(self):
        return self.Libelle


class Filiere(models.Model):
    Libelle = models.CharField(max_length=300)

    def __str__(self):
        return self.Libelle


class Cour(models.Model):
    Libelle = models.CharField(max_length=300)

    def __str__(self):
        return self.Libelle


metier = [
    ("TIC", "tic"),
    ("MA", "ma"),

]


class Formateur(models.Model):
    name = models.CharField(max_length=200)
    metiers = models.CharField(choices=metier, max_length=50)

    def __str__(self):
        return self.name


class Planning(models.Model):
    date = models.DateField( )
    heuredebut = models.TimeField()
    heurefin = models.TimeField()
    activite = models.ForeignKey(Cour, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    formateur = models.ForeignKey(Formateur, on_delete=models.CASCADE)
    salls = models.ForeignKey(Salle, on_delete=models.CASCADE)
    promo = models.CharField(max_length=300)
    Annee = models.CharField(max_length=300)
    Semaine = models.CharField(max_length=300)

    def __str__(self):
        return self.date
