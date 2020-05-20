from django.contrib.auth.views import (
    LoginView,
    LogoutView,
)
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from django.urls import reverse_lazy
from .lib import mixins
from .constants import urls_name


class CustomLoginView(mixins.OnlyLoggedOut, LoginView):
    template_name = "a_core/login.html"


class CustomLogoutView(mixins.OnlyLoggedIn, LogoutView):
    # 로그아웃을 한 이후에 보여줄 template 이름
    # settings.py 에 LOGOUT_REDIRECT_URL 를 명시해주면 이 값을 우선적으로 따라간다.
    template_name = "a_core/logout.html"


class RegisterUser(mixins.OnlyLoggedOut, FormView):
    template_name = "a_core/register.html"
    success_url = reverse_lazy(f"{urls_name.APP_NAME}{urls_name.AFTER_REGISTER}")
    form_class = UserCreationForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get("username")
        raw_password = form.cleaned_data.get("password1")
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super().form_valid(form)
