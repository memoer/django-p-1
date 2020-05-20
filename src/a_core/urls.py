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
        CustomLogoutView.as_view(template_name="a_core/logout.html"),
        name=urls_name.LOGOUT,
    ),
    path("register/", RegisterUser.as_view(), name=urls_name.REGISTER),
    path(
        "passwordChange/",
        PasswordChangeView.as_view(
            template_name="a_core/password_change.html",
            success_url=reverse_lazy(
                f"{urls_name.APP_NAME}:{urls_name.PASSWORD_CHANGE_DONE}"
            ),
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
    path(
        "passwordReset/",
        PasswordResetView.as_view(
            template_name="a_core/password_reset.html",
            email_template_name="a_core/password_reset_email.html",
            subject_template_name="a_core/password_reset_subject.txt",
            success_url=reverse_lazy(
                f"{urls_name.APP_NAME}:{urls_name.PASSWORD_RESET_DONE}"
            ),
        ),
        name=urls_name.PASSWORD_RESET,
    ),
    path(
        "passwordResetDone/",
        PasswordResetDoneView.as_view(template_name="a_core/password_reset_done.html"),
        name=urls_name.PASSWORD_RESET_DONE,
    ),
    path(
        "passwordResetConfirm/<uidb64>/<token>/",
        PasswordResetConfirmView.as_view(
            template_name="a_core/password_reset_confirm.html",
            success_url=reverse_lazy(
                f"{urls_name.APP_NAME}:{urls_name.PASSWORD_RESET_COMPLETE}"
            ),
        ),
        name=urls_name.PASSWORD_RESET_CONFIRM,
    ),
    path(
        "passwordResetComplete/",
        PasswordResetCompleteView.as_view(
            template_name="a_core/password_reset_complete.html"
        ),
        name=urls_name.PASSWORD_RESET_COMPLETE,
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
