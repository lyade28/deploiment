from rest_framework import serializers

from isep.models import *


class SemaineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semaine
        fields = "__all__"
        depth = 2


class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = "__all__"
        depth = 1


class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = "__all__"
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


class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planning
        fields = "__all__"
        depth = 1


class FilliereMetierSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilliereMetier
        fields = "__all__"
        depth = 1
