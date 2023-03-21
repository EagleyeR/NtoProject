from django.urls import path
from .views import *
from rest_framework.authtoken import views


urlpatterns = [
    path('publish', publish_message, name="publish"),
    path('login/', views.obtain_auth_token, name="login"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('full/', AdminView.as_view(), name="full_info"),
    path('for_user/', UserView.as_view(), name="user_info"),
]
