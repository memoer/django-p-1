from django.urls import path
from django.views.generic.base import TemplateView
from django.contrib.auth.views import (
    PasswordChangeView,
    PasswordChangeDoneView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)
from django.urls import reverse_lazy
from .constant import urls_name as name
from .views import (
    RegisterUser,
    CustomLoginView,
    CustomLogoutView,
)


app_name = name.APP_NAME
urlpatterns = [
    path("", TemplateView.as_view(template_name="a_core/home.html"), name=name.HOME),
    path(
        "login/",
        CustomLoginView.as_view(template_name="a_core/login.html"),
        name=name.LOGIN,
    ),
    path(
        "logout/",
        CustomLogoutView.as_view(template_name="a_core/logout.html"),
        name=name.LOGOUT,
    ),
    path("register/", RegisterUser.as_view(), name=name.REGISTER),
    path(
        "passwordChange/",
        PasswordChangeView.as_view(
            template_name="a_core/password_change.html",
            success_url=reverse_lazy(f"{name.APP_NAME}:{name.PASSWORD_CHANGE_DONE}"),
        ),
        name=name.PASSWORD_CHANGE,
    ),
    path(
        "passwordChangeDone/",
        PasswordChangeDoneView.as_view(
            template_name="a_core/password_change_done.html"
        ),
        name=name.PASSWORD_CHANGE_DONE,
    ),
    path(
        "passwordReset/",
        PasswordResetView.as_view(
            template_name="a_core/password_reset.html",
            email_template_name="a_core/password_reset_email.html",
            subject_template_name="a_core/password_reset_subject.txt",
            success_url=reverse_lazy(f"{name.APP_NAME}:{name.PASSWORD_RESET_DONE}"),
        ),
        name=name.PASSWORD_RESET,
    ),
    path(
        "passwordResetDone/",
        PasswordResetDoneView.as_view(template_name="a_core/password_reset_done.html"),
        name=name.PASSWORD_RESET_DONE,
    ),
    path(
        "passwordResetConfirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="a_core/password_reset_confirm.html",
            success_url=reverse_lazy(f"{name.APP_NAME}:{name.PASSWORD_RESET_COMPLETE}"),
        ),
        name=name.PASSWORD_RESET_CONFIRM,
    ),
    path(
        "passwordResetComplete/",
        PasswordResetCompleteView.as_view(
            template_name="a_core/password_reset_complete.html"
        ),
        name=name.PASSWORD_RESET_COMPLETE,
    ),
    #
    path(
        "after/login",
        TemplateView.as_view(template_name="a_core/after/login.html"),
        name=name.AFTER_LOGIN,
    ),
    path(
        "after/logout",
        TemplateView.as_view(template_name="a_core/after/logout.html"),
        name=name.AFTER_LOGOUT,
    ),
    path(
        "after/register",
        TemplateView.as_view(template_name="a_core/after/register.html"),
        name=name.AFTER_REGISTER,
    ),
]
