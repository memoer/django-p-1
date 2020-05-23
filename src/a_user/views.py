from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User


class UserListView(ListView):
    model = User
    paginate_by = 5
    template_name = "a_user/list.html"
    context_object_name = "users"


class UserDetailView(DetailView):
    model = User
    context_object_name = "user"
    template_name = "a_user/detail.html"
