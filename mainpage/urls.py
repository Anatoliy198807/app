from django.urls import path

from .views import index_view, post_list_view, post_detail_view

urlpatterns = [
    path("", index_view),
    path("all-posts/", post_list_view, name ="post_list"),
    path("posts/<int:post_id>/", post_detail_view, name = "post_detail")
]
