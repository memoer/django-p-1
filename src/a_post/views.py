from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .constant import urls_name as name
from common.constant import urls_name as common_name
from .lib.mixins import OnlyCreatedBy
from .models import Post


class PostListView(ListView):
    model = Post
    paginate_by = 5
    context_object_name = "posts"
    template_name = "a_post/list.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "a_post/detail.html"


@method_decorator(login_required, name="dispatch")
class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    template_name = "a_post/create.html"

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.created_by = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


@method_decorator(login_required, name="dispatch")
class PostUpdateView(OnlyCreatedBy, UpdateView):
    model = Post
    fields = "__all__"
    template_name = "a_post/update.html"


@method_decorator(login_required, name="dispatch")
class PostDeleteView(OnlyCreatedBy, DeleteView):
    model = Post
    template_name = "a_post/delete.html"
    success_url = reverse_lazy(f"{name.APP_NAME}:{common_name.AFTER_DELETE}")
