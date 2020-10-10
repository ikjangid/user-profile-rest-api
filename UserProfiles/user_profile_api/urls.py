from django.urls import path

from user_profile_api import views

urlpatterns = [
    path('api-view/', views.MyApiView.as_view()),
]