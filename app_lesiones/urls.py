from django.urls import path
from . import views

urlpatterns = [

    # API REST
    path('api/lesiones/', views.api_lesiones, name='api_lesiones'),
    path('api/clima/', views.api_clima, name='api_clima'),


    # PANEL PRINCIPAL
    path('', views.panel_inicio, name='panel'),
    path('panel-entrenador/', views.panel_entrenador, name='panel_entrenador'),
    path('panel-kinesio/', views.panel_kinesio, name='panel_kinesio'),

    # ESTUDIANTES (solo entrenadores)
    path('estudiantes/', views.lista_estudiantes, name='lista_estudiantes'),
    path('estudiantes/crear/', views.crear_estudiante, name='crear_estudiante'),
    path('estudiantes/editar/<int:id>/', views.editar_estudiante, name='editar_estudiante'),
    path('estudiantes/eliminar/<int:id>/', views.eliminar_estudiante, name='eliminar_estudiante'),

    # LESIONES (entrenadores y kinesiólogos)
    path('lesiones/', views.lista_lesiones, name='lista_lesiones'),
    path('lesiones/crear/', views.crear_lesion, name='crear_lesion'),
    path('lesiones/editar/<int:id>/', views.editar_lesion, name='editar_lesion'),
    path('lesiones/eliminar/<int:id>/', views.eliminar_lesion, name='eliminar_lesion'),

    # TRATAMIENTOS (solo kinesiólogos)
    path('tratamientos/', views.lista_tratamientos, name='lista_tratamientos'),
    path('tratamientos/crear/', views.crear_tratamiento, name='crear_tratamiento'),
    path('tratamientos/editar/<int:id>/', views.editar_tratamiento, name='editar_tratamiento'),
    path('tratamientos/eliminar/<int:id>/', views.eliminar_tratamiento, name='eliminar_tratamiento'),
]
