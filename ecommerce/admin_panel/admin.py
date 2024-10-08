from django.contrib import admin
from .models import (
    ContactUs,
    Coupon,
    Banner,
    Address,
    EmailTemplate,
    Banner,
    NewsLetter,
)
from django.contrib.auth.models import Permission


# Register your models here.


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "type",
        "country",
        "state",
        "city",
        "pincode",
        "street_address",
        "apartment_number",
        "phone_number",
        "active",
        "default",
    ]


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "image",
        "url",
        "is_active",
        "status",
        "created_at",
        "updated_at",
        "deleted_at",
    ]


@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "user",
        "first_name",
        "last_name",
        "email",
        "phone_number",
        "message",
        "created_at",
    ]


@admin.register(Coupon)
class CouponAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "code",
        "name",
        "count",
        "is_active",
        "description",
        "discount",
        "start_date",
        "end_date",
        "created_at",
        "updated_at",
        "deleted_at",
    ]


@admin.register(EmailTemplate)
class EmailTemplateAdmin(admin.ModelAdmin):
    list_display = [
        "id",
        "title",
        "subject",
        "content",
        "created_at",
        "updated_at",
        "deleted_at",
    ]


@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    list_display = ("name", "content_type", "codename")
    search_fields = ("name", "codename")


@admin.register(NewsLetter)
class NewsLetterAdmin(admin.ModelAdmin):
    list_display = ["id", "email", "created_at"]
    search_fields = ("email",)
