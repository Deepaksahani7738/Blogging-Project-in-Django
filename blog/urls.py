from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='home'),
    path('post_detail/<int:pk>/',views.post_detail_views,name='post_detail'),
    path('post/new/',views.post_new,name='post_new'),
    path('post/edit/<int:pk>/',views.post_edit,name='post_edit'),
    path('post/delete/<int:pk>/',views.post_delete,name='post_delete'),
    path('login/',auth_views.LoginView.as_view(template_name='login.html'),name='login'),
    path('register/',views.register,name='register'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),name='password_reset_complete'),
    path('logout',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
]
