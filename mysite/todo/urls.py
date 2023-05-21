from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("insert/", views.insert, name="insert"),
    path("update/", views.update, name="update"),
    path("view/", views.view, name="view"),
    path("viewOne/",views.view_single_item, name="viewOne"),
    path("delete/",views.delete_item,name="delete")
]