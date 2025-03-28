from django.urls import path

from .views import VehiculoApiView

urlpatterns = [
    path ('crear',VehiculoApiView.as_view()),
    path ('obtener-todos',VehiculoApiView.as_view()),
    path ('actualizar/<int:pkid>',VehiculoApiView.as_view(),name='actualizar_vehiculo'),
    path ('eliminar/<int:pkid>',VehiculoApiView.as_view(),name='eliminar_vehiculo'),
]
