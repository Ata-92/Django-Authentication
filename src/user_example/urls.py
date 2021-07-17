from django.urls import path

from user_example.views import home_view, register, special

urlpatterns = [
    path('', home_view, name="home"),
    path('special/', special, name="special_view"),
    path('register/', register, name="register"),
]
