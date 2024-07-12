from django.urls import path
from . import views

app_name = 'blog'

urlpatters = [
    path("", views.post_list, name="post_list"),
    path("<int:id>/", views.get_object_or_404, name="post_details"),
]
