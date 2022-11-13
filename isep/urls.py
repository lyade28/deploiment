from django.urls import path
from .views import *

urlpatterns = [

    path('salle', SalleList.as_view(), name='sall_liste'),
    path('salle/<int:pk>', Salledestail.as_view(), name='sall_detail'),
    path('filiere', FiliereList.as_view(), name='Filiere_list'),
    path('filiere/<int:pk>', Filieredestail.as_view(), name='Filiere_details'),
    path('cour', CourList.as_view(), name='Cour_list'),
    path('cour/<int:pk>', Courdestail.as_view(), name='Cour_details'),
    path('formateur', FormateurList.as_view(), name='Formateur_list'),
    path('formateur/<int:pk>', Formateurdestail.as_view(), name='Formateur_details'),
    path('planning', PlanningList.as_view(), name='planning_list'),
    path('planning/<int:pk>', Planningdestail.as_view(), name='planning_details'),
]
