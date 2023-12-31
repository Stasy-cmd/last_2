from django.contrib import admin
from django.contrib.auth import get_user_model

from .models import Subscription

User = get_user_model()


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "email",
        "username",
        "first_name",
        "last_name",
        "password",
        "date_joined",
    )
    list_filter = ("email", "first_name")
    empty_value_display = "--None--"
    search_fields = ("^email",)


@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ("user", "following")
    empty_value_display = "--None--"
    search_fields = ("user",)
    list_filter = ("user", "following")
