 from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Authentication URLs
    path('', views.CustomLoginView.as_view(), name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    
    # Password reset URLs
    path('password-reset/', 
         auth_views.PasswordResetView.as_view(
             template_name='calificaciones/password_reset.html',
             email_template_name='calificaciones/password_reset_email.html',
             subject_template_name='calificaciones/password_reset_subject.txt',
             success_url='/password-reset/done/'
         ), 
         name='password_reset'),
    path('password-reset/done/', 
         auth_views.PasswordResetDoneView.as_view(
             template_name='calificaciones/password_reset_done.html'
         ), 
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', 
         auth_views.PasswordResetConfirmView.as_view(
             template_name='calificaciones/password_reset_confirm.html',
             success_url='/password-reset-complete/'
         ), 
         name='password_reset_confirm'),
    path('password-reset-complete/', 
         auth_views.PasswordResetCompleteView.as_view(
             template_name='calificaciones/password_reset_complete.html'
         ), 
         name='password_reset_complete'),
    
    # CRUD URLs
    path('calificaciones/', views.listar_calificaciones, name='listar_calificaciones'),
    path('calificaciones/crear/', views.crear_calificacion, name='crear_calificacion'),
    path('calificaciones/editar/<int:pk>/', views.editar_calificacion, name='editar_calificacion'),
    path('calificaciones/eliminar/<int:pk>/', views.eliminar_calificacion, name='eliminar_calificacion'),
]
