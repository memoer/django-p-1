from django.urls import path
from django.views.generic.base import TemplateView
from .constant import urls_name as name
from common.constant import urls_name as common_name
from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
)

app_name = name.APP_NAME
urlpatterns = [
    path("", PostListView.as_view(), name=common_name.LIST),
    path("<int:pk>/", PostDetailView.as_view(), name=common_name.DETAIL),
    path("create/", PostCreateView.as_view(), name=common_name.CREATE),
    path("<int:pk>/update/", PostUpdateView.as_view(), name=common_name.UPDATE),
    path("<int:pk>/delete/", PostDeleteView.as_view(), name=common_name.DELETE),
    path(
        "delete/after/",
        TemplateView.as_view(template_name="a_post/after/delete.html"),
        name=common_name.AFTER_DELETE,
    ),
]
