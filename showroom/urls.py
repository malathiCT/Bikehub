from django.urls import path

from . import api_views, views

urlpatterns = [
    path("", views.home, name="home"),
    path("bike/<int:id>/", views.bike_detail, name="bike-detail"),
    path("api/bikes/", api_views.bike_list, name="bike-list"),
    path("api/bikes/<int:id>/", api_views.bike_detail, name="bike-detail-api"),
    path("api/bikes/create/", api_views.bike_create, name="bike-create"),
    path("api/bikes/<int:id>/update/", api_views.bike_update, name="bike-update"),
    path("api/bikes/<int:id>/delete/", api_views.bike_delete, name="bike-delete"),
]