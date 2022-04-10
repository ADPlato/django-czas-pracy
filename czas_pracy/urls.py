"""czas_pracy URL Configuration

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
from django.contrib.auth import views as auth_views


from ewidencja.views import index_view,employees_view, managers_view, time_view, project_view, teams_view, add_worktime_report

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index_view),
    path('login', auth_views.LoginView.as_view()),
    path('employees', employees_view),
    path('mamagers', managers_view),
    path('working-time',add_worktime_report),
    path('projects', project_view),
    path('teams', teams_view),
]
