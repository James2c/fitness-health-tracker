from django.urls import path

from . import views


urlpatterns = [
    path("", views.nutrition_list, name="nutrition_list"),
    path("add/", views.nutrition_create, name="nutrition_create"),
    path("goals/", views.nutrition_goals, name="nutrition_goals"),
    path(
        "<int:entry_id>/edit/",
        views.nutrition_edit,
        name="nutrition_edit",
    ),
    path(
        "<int:entry_id>/delete/",
        views.nutrition_delete,
        name="nutrition_delete",
    ),
]