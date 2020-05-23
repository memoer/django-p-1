from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from .constant import urls_name as name
from common.constant import urls_name as common_name
from common.models import TimeStampedModel


class Post(TimeStampedModel):
    title = models.CharField(
        blank=False, null=False, help_text="post title", max_length=255,
    )
    content = models.TextField(blank=False, null=False, help_text="post content")
    # editable is false, the field will not be displayed in the admin or any other ModelForm
    liked = models.IntegerField(
        blank=True, null=False, default=0, help_text="liked numbers", editable=False
    )
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, null=False, editable=False
    )

    class Meta:
        db_table = "post"

    def get_absolute_url(self):
        return reverse(f"{name.APP_NAME}:{common_name.DETAIL}", kwargs={"pk": self.pk})
