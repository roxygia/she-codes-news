from django.urls import path
from .views import CreateAccountView
from .views import AccountProfileView

app_name = 'users'

urlpatterns = [
    path('create-account/', CreateAccountView.as_view(), name='createAccount'),
    path('profile/<int:pk>', AccountProfileView.as_view(), name='accountProfile'),
    path('profile/<str:slug>', AccountProfileView.as_view(), name='accountProfile'),
]