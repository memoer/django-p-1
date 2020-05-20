import os

FRONT_END_PATH = os.path.join(
    os.path.dirname(os.path.abspath(os.path.join(__file__, "..", "..", ".."))),
    "frontend",
)
TEMPLATE_DIRS_PATH = os.path.join(FRONT_END_PATH, "templates")
STATICFILES_DIRS = [os.path.join(FRONT_END_PATH, "statics")]
ADMINS = [("Jaenam"), "hanjn2842@naver.com"]
MEDIA_ROOT = os.path.join(FRONT_END_PATH, "uploads")
MEDIA_URL = "/media/"
LOGOUT_REDIRECT_URL = "/after/logout"
LOGIN_REDIRECT_URL = "/after/login"
# login_required(login_url=) 만약 인자로 login_url를 주지 않을 경우 아래에 설정된 url로 redirect 된다.
LOGIN_URL = "/login"
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
