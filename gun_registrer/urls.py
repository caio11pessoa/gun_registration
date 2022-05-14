from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from gun_registrer import views

urlpatterns = format_suffix_patterns([
    path('calibres/', views.Calibre.as_view(), name='calibre-list')
])
