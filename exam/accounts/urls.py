from django.urls import path
from accounts.views.login import login_view, logout_view, register_view
from accounts.views.profile import UserUpdateView, UserChangePasswordView, UserDetailView

app_name = 'accounts'

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('create/', register_view, name='create_acc'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user_profile'),
     path('profile/edit/', UserUpdateView.as_view(), name='user-update-profile'),
    path('change-password/', UserChangePasswordView.as_view(), name='user-change-password')
]

