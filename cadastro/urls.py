
from django.contrib import admin
from django.urls import path
from base.views import cadastro

urlpatterns = [
    path('', cadastro),
    path('admin/', admin.site.urls),
]
