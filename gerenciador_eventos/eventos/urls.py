from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('eventos/', views.listar_eventos, name='listar_eventos'),
    path('eventos/criar/', views.criar_evento, name='criar_evento'),
    path('eventos/<int:pk>/', views.detalhar_evento, name='detalhar_evento'),
    path('eventos/editar/<int:pk>/', views.editar_evento, name='editar_evento'),
    path('eventos/excluir/<int:pk>/', views.excluir_evento, name='excluir_evento'),
    path('participantes/', views.listar_participantes, name='listar_participantes'),
    path('participantes/criar/', views.criar_participante, name='criar_participante'),
    path('participantes/editar/<int:pk>/', views.editar_participante, name='editar_participante'),
    path('participantes/excluir/<int:pk>/', views.excluir_participante, name='excluir_participante'),
]