from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import reverse_lazy
from .constants import urls_name
from .views import (
    RegisterUser,
    CustomLoginView,
    CustomLogoutView,
)


app_name = urls_name.APP_NAME
urlpatterns = [
    path(
        "", TemplateView.as_view(template_name="a_core/home.html"), name=urls_name.HOME
    ),
    path(
        "login/",
        CustomLoginView.as_view(template_name="a_core/login.html"),
        name=urls_name.LOGIN,
    ),
    path(
        "logout/",
        # login_url 이 "/1" 이라서 localhost:8000/1/?next=/logout/ 으로 표시된다.
        # 말 그대로 login을 하려는 url 이 어딘 지 표시해주는 것.
        # login_required(
        #     LogoutView.as_view(template_name="a_core/logout.html"), login_url="/1"
        # ),
        CustomLogoutView.as_view(template_name="a_core/logout.html"),
        name=urls_name.LOGOUT,
    ),
    path("register/", RegisterUser.as_view(), name=urls_name.REGISTER),
    path(
        "passwordChange/",
        PasswordChangeView.as_view(
            template_name="a_core/password_change.html",
            success_url=reverse_lazy(f"A_CORE:PASSWORD_CHANGE_DONE"),
        ),
        name=urls_name.PASSWORD_CHANGE,
    ),
    path(
        "passwordChangeDone/",
        PasswordChangeDoneView.as_view(
            template_name="a_core/password_change_done.html"
        ),
        name=urls_name.PASSWORD_CHANGE_DONE,
    ),
    #
    path(
        "after/login",
        TemplateView.as_view(template_name="a_core/after/login.html"),
        name=urls_name.AFTER_LOGIN,
    ),
    path(
        "after/logout",
        TemplateView.as_view(template_name="a_core/after/logout.html"),
        name=urls_name.AFTER_LOGOUT,
    ),
    path(
        "after/register",
        TemplateView.as_view(template_name="a_core/after/register.html"),
        name=urls_name.AFTER_REGISTER,
    ),
]
