from django.urls import path

from user_example.views import home_view, special

urlpatterns = [
    path('', home_view, name="home"),
    path('special/', special, name="special_view"),
]
