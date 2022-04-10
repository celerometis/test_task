from django.urls import path

from . import views

urlpatterns = [
    path('', views.ContactListCreateAPIView.as_view()),
    path('<int:pk>/', views.ContactDetailAPIView.as_view()),
    path('<int:pk>/update/', views.ContactUpdateAPIView.as_view()),
    path('<int:pk>/delete/', views.ContactDestroyAPIView.as_view()),
    # functional api
    path('functional/', views.contact_crl_view),
    path('functional/<int:pk>/', views.contact_crl_view),
]
