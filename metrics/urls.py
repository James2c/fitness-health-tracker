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

    path(
        "weight/<int:entry_id>/edit/",
        views.weight_edit,
        name="weight_edit",
    ),

    path(
        "weight/<int:entry_id>/delete/",
        views.weight_delete,
        name="weight_delete",
    ),

]