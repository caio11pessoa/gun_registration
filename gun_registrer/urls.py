from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from gun_registrer import views
from gun_registrer.models import Arma, Municao, Objeto_tipo

urlpatterns = format_suffix_patterns([
    path('calibres/', views.Calibre.as_view(), name='calibre-list'),
    path('armas/', views.Arma.as_view(), name='calibre-list'),
    path('municoes/', views.Municao.as_view(), name='calibre-list'),
    path('objeto_tipos/', views.Objeto_tipo.as_view(), name='calibre-list'),
])
