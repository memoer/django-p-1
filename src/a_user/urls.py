from django.urls import path
from .constant import urls_name as name
from common.constant import urls_name as common_name
from .views import UserListView, UserDetailView


app_name = name.APP_NAME
urlpatterns = [
    path("", UserListView.as_view(), name=common_name.LIST),
    path("<int:pk>/", UserDetailView.as_view(), name=common_name.DETAIL),
]
