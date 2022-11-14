from rest_framework import serializers

from isep.models import *


class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planning
        fields = "__all__"
        depth = 1


class SemaineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semaine
        fields = ['id', 'code', 'metier', 'promo', 'filiereMetier']
        depth = 3


class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = "__all__"
        depth = 1


class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = ['id', 'libelle', 'metier', 'planning']
        depth = 1


class CourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cour
        fields = "__all__"
        depth = 1


class FormateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formateur
        fields = "__all__"
        depth = 1


class FilliereMetierSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilliereMetier
        fields = "__all__"
        depth = 1
