from django.urls import path
from . import views

app_name = 'testapp'

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('features/', views.features_view, name='features'),
    path('signup/', views.signup_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('upload_video/',views.upload_videoView, name='upload_video'),
]
