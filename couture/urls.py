"""
URL configuration for couture project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from TNC import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.mesure, name='mesure-liste'),
    path('mesure_detail/<int:id>/', views.mesure_detail, name="mesure-detail"),
    path('mesure/add/',views.mesure_create, name='mesure-create'),
    path('mesure/<int:id>/change/', views.mesure_update, name="mesure-update"),
    path('mesure/<int:id>/delete/', views.mesure_delete, name="mesure-delete"),
    path('commande/', views.commande,name='commande-liste'),
    path('commande_detail/<int:id>/', views.commande_detail,name='commande-detail'),
    path('commande/add/', views.commande_create,name='commande-create'),
    path('commande/<int:id>/change/', views.commande_update,name='commande-update'),
    path('contact/', views.contact),
]
