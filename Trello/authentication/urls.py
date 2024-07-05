from django.urls import path
from . import views

urlpatterns = [
    path('auth/signup/', views.signup),
    path('auth/login/', views.custom_obtain_auth_token),
    path('users/<int:pk>/profile/', views.UserProfileDetailUpdate.as_view()),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('users/<int:pk>/update/', views.UserUpdate.as_view(), name='user-update'),
    path('users/<int:pk>/delete/', views.UserDelete.as_view(), name='user-delete'),
    path('users/create/', views.UserCreate.as_view(), name='user-create'),
]
