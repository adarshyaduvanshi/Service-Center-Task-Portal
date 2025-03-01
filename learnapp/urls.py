from django.urls import path
from learnapp import views

urlpatterns = [
    path('',views.register,name='register'),
    path('login/',views.user_login,name='login'),
    path('home/',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('edit/',views.userEdit,name='edit'),
    path('logout/',views.user_logout,name='logout'),
]