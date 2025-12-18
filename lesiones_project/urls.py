from django.contrib import admin
from django.urls import path, include
from cuentas import views as cuentas_views
from app_lesiones import views as lesiones_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Login
    path('login/', cuentas_views.login_view, name='login'),
    path('logout/', cuentas_views.logout_view, name='logout'),
    path('registro/', cuentas_views.registro, name='registro'),

    # Página principal
    path('', lesiones_views.panel_inicio, name='panel'),

    # URLs de la app (HTML)
    path('', include('app_lesiones.urls')),
]
