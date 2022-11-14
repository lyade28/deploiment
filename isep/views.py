from django.shortcuts import render
from rest_framework import generics

from .models import *
from .serializer import *


# Create your views here.


class SalleList(generics.ListCreateAPIView):
    queryset = Salle.objects.all()
    serializer_class = SalleSerializer


class Salledestail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Salle
    serializer_class = SalleSerializer


class FiliereList(generics.ListCreateAPIView):
    queryset = Salle.objects.all()
    serializer_class = FiliereSerializer


class Filieredestail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Filiere
    serializer_class = FiliereSerializer


class CourList(generics.ListCreateAPIView):
    queryset = Cour.objects.all()
    serializer_class = CourSerializer


class Courdestail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cour
    serializer_class = CourSerializer


class FormateurList(generics.ListCreateAPIView):
    queryset = Formateur.objects.all()
    serializer_class = FormateurSerializer


class Formateurdestail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Formateur
    serializer_class = FormateurSerializer


class PlanningList(generics.ListCreateAPIView):
    queryset = Planning.objects.all()
    serializer_class = PlanningSerializer


class Planningdestail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Planning
    serializer_class = PlanningSerializer


class SemaineList(generics.ListCreateAPIView):
    queryset = Semaine.objects.all()
    serializer_class = SemaineSerializer


class Semainedestail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Semaine
    serializer_class = SemaineSerializer


class FilliereMetierList(generics.ListCreateAPIView):
    queryset = FilliereMetier.objects.all()
    serializer_class = FilliereMetierSerializer


class FilliereMetierdestail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FilliereMetier
    serializer_class = FilliereMetierSerializer
