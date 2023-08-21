from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_page, name="login"),
    path("logout", views.logout_page, name="logout"),
    path("register", views.register, name="register"),
    path("new_activity", views.new_activity, name="new_activity"),
    path("activities/<str:time>", views.activities, name="activities"),
    path("delete_activity/<int:activity_id>", views.delete_activity, name="delete"),
]