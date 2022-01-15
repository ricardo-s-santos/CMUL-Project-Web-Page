from django.urls import path
from . import views

app_name = "website"

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('evolucao/', views.evolucao, name='evolucao'),
    path('tecnologia/', views.tecnologia, name='tecnologia'),
    path('bussiness_models/', views.bussiness_models, name='bussiness_models'),
    path('interfaces/', views.interfaces, name='interfaces'),
    path('impactos_sociais/', views.impactos_sociais, name='impactos_sociais'),
    path('impactos_eticos/', views.impactos_eticos, name='impactos_eticos'),
    path('portugal/', views.portugal, name='portugal'),
    path('futuro/', views.futuro, name='futuro'),
]
