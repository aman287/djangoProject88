"""djangoProject88 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from app88 import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.showIndex),
    path('register/', views.registerEmployee, name='register'),
    path('save/', views.saveEmployee, name='save'),
    path('view/', views.viewallEmployee, name='viewall'),
    path('update/', views.updateEmployee, name='update'),
    path('update_emp/', views.update_emp, name='update_emp'),
    path('delete/', views.deleteEmp, name='delete'),
]
