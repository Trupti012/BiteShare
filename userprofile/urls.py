from django.urls import path
from .views import home_view
from .views import login_view
from .views import signup_view
from .views import logout_view,profile_view

urlpatterns = [
    path('home/',home_view,name="home_view"),
    path('login/',login_view,name="login_view"),
    path('signup/',signup_view,name="signup_view"),
    path('logout/',logout_view,name="logout_view"),
    path('profile/<str:username>/',profile_view,name="profile_view"),
    
]