from django.urls import path
from . import views

app_name = 'crud_project'
urlpatterns = [
    path('', views.index, name="login"),
    path('dashboard', views.dashboard, name="dash"),
    path('register', views.register, name="reg"),
    path('viewusers', views.users, name="view"),
]
