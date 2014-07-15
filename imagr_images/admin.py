from django.contrib import admin
from imagr_images.models import (
    Photo,
    Album,
)
from imagr_users.models import ImagrUser


admin.site.register(Photo)
admin.site.register(Album)
admin.site.register(ImagrUser)
