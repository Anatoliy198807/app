from django.urls import path

from .views import index_view, post_list_view, post_detail_view, create_post_view, edit_post_view, delete_post_view


app_name='mainpage'
urlpatterns = [
    path("", index_view, name = 'index'),
    path("all-posts/", post_list_view, name ="post_list"),
    path("posts/<int:post_id>/", post_detail_view, name = "post_detail"),
    path("posts/add/", create_post_view, name = "post_create"),
    path("posts/<int:post_id>/edit/", edit_post_view, name = "post_edit"),
    path("posts/<int:post_id>/delete", delete_post_view, name = 'delete_post')
]
