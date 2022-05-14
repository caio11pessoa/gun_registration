from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from gun_registrer import views

urlpatterns = format_suffix_patterns([
    path('calibres/', views.CalibreList.as_view(), name='calibre-list'),
    path('calibres/<int:pk>', views.CalibreDetail.as_view(),
         name='calibre-detail'),
    path('armas/', views.ArmaList.as_view(), name='arma-list'),
    path('armas/<int:pk>', views.ArmaDetail.as_view(), name='arma-detail'),
    path('municoes/', views.MunicaoList.as_view(), name='Municao-list'),
    path('municoes/<int:pk>', views.MunicaoDetail.as_view(),
         name='Municao-detail'),
    path('objeto_tipos/<int:pk>', views.Objeto_tipoList.as_view(),
         name='objeto_tipo-list'),
    path('objeto_tipos/<int:pk>', views.Objeto_tipoDetail.as_view(),
         name='objeto_tipo-detail'),
])
