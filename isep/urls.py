from django.urls import path
from .views import *

urlpatterns = [

    path('salles', SalleList.as_view(), name='sall_liste'),
    path('salles/<int:pk>', Salledestail.as_view(), name='sall_detail'),
    path('filieres', FiliereList.as_view(), name='Filiere_list'),
    path('filieres/<int:pk>', Filieredestail.as_view(), name='Filiere_details'),
    path('cours', CourList.as_view(), name='Cour_list'),
    path('cours/<int:pk>', Courdestail.as_view(), name='Cour_details'),
    path('formateurs', FormateurList.as_view(), name='Formateur_list'),
    path('formateurs/<int:pk>', Formateurdestail.as_view(), name='Formateur_details'),
    path('planning', PlanningList.as_view(), name='planning_list'),
    path('planning/<int:pk>', Planningdestail.as_view(), name='planning_details'),
    path('semaines', SemaineList.as_view(), name='semaine_list'),
    path('semaines/<int:pk>',  Semainedestail.as_view(), name='semaine_details'),
    path('filliereMetiers', FilliereMetierList.as_view(), name='filliereMetiers_list'),
    path('filliereMetiers/<int:pk>', FilliereMetierdestail.as_view(), name='sfilliereMetiers_details'),
]
