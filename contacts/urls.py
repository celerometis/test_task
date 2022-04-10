from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactMixinView.as_view()),
    path('<int:pk>/', views.ContactMixinView.as_view()),

]
