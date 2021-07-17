from django.urls import path

from user_example.views import home_view

urlpatterns = [
    path('', home_view, name="home"),
]
