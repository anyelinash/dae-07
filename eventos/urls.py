from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_eventos, name='lista_eventos'),
    path('crear/', views.crear_evento, name='crear_evento'),
    path('eventos/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('eventos/<int:evento_id>/editar/', views.editar_evento, name='editar_evento'),
    path('eventos/<int:evento_id>/eliminar/', views.eliminar_evento, name='eliminar_evento'),
    path('registrar_evento/', views.registrar_evento, name='registrar_evento'),
    path('registrar_usuario/', views.registrar_usuario, name='registrar_usuario'),
    path('registro/<int:registro_id>/editar/', views.editar_registro_evento, name='editar_registro_evento'),
    path('registro/<int:registro_id>/eliminar/', views.eliminar_registro_evento, name='eliminar_registro_evento'),
]