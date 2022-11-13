from rest_framework import serializers

from isep.models import *


class SalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salle
        fields = "__all__"


class FiliereSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filiere
        fields = "__all__"


class CourSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cour
        fields = "__all__"


class FormateurSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formateur
        fields = "__all__"


class PlanningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Planning
        fields = "__all__"
        depth = 1
