from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('login',views.login, name="login"),
    path('signup',views.signup, name="signup"),
    path('logout',views.logout_view, name="logout"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('dashboard/map',views.map, name="map"),
    path('dashboard/festivals',views.festival, name="festival"),
    path('dashboard/events',views.event, name="event"),
    path('dashboard/chat',views.chat, name="chat"),
]