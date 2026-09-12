from django.urls import path

from . import views


urlpatterns = [
    path(
        "weight/",
        views.weight_list,
        name="weight_list",
    ),

    path(
        "weight/add/",
        views.weight_create,
        name="weight_create",
    ),
]