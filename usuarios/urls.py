from django.urls import path
from . import views
urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('', views.login_view, name='login'),
    path('sair/', views.sair, name="sair"),
]