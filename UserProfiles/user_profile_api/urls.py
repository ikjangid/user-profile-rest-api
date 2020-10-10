from django.urls import path, include


from rest_framework.routers import DefaultRouter

from user_profile_api import views

router = DefaultRouter()
router.register('my-viewset', views.MyViewSet, basename='my-viewset')
router.register('profile', views.ProfileViewSet)

urlpatterns = [
    path('api-view/', views.MyApiView.as_view()),
    path('login/', views.LoginApiView.as_view()),
    path('', include(router.urls))
]