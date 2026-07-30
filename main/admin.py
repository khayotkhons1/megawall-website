from django.contrib import admin

from .models import Product, Contact


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "is_featured",
        "is_active",
        "order",
        "created_at",
    )

    list_display_links = (
        "name",
    )

    list_filter = (
        "category",
        "is_featured",
        "is_active",
        "created_at",
    )

    search_fields = (
        "name",
        "short_description",
        "description",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    ordering = (
        "order",
        "name",
    )

    list_editable = (
        "is_featured",
        "is_active",
        "order",
    )

    readonly_fields = (
        "created_at",
        "updated_at",
    )

    date_hierarchy = "created_at"

    list_per_page = 25

    save_on_top = True

    empty_value_display = "-"

    fieldsets = (

        (
            "Asosiy ma'lumotlar",
            {
                "fields": (
                    "name",
                    "slug",
                    "category",
                )
            }
        ),

        (
            "Tavsif",
            {
                "fields": (
                    "short_description",
                    "description",
                )
            }
        ),

        (
            "Mahsulot rasmi",
            {
                "fields": (
                    "image",
                )
            }
        ),

        (
            "Sozlamalar",
            {
                "fields": (
                    "is_featured",
                    "is_active",
                    "order",
                )
            }
        ),

        (
            "Tizim ma'lumotlari",
            {
                "fields": (
                    "created_at",
                    "updated_at",
                ),
                "classes": (
                    "collapse",
                ),
            }
        ),

    )
    @admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "phone",
        "subject",
        "is_read",
        "created_at",
    )

    list_display_links = (
        "name",
    )

    list_filter = (
        "is_read",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
        "phone",
        "subject",
        "message",
    )

    ordering = (
        "-created_at",
    )

    list_editable = (
        "is_read",
    )

    readonly_fields = (
        "created_at",
    )

    date_hierarchy = "created_at"

    list_per_page = 25

    save_on_top = True

    empty_value_display = "-"

    fieldsets = (

        (
            "Mijoz ma'lumotlari",
            {
                "fields": (
                    "name",
                    "email",
                    "phone",
                )
            }
        ),

        (
            "Murojaat",
            {
                "fields": (
                    "subject",
                    "message",
                )
            }
        ),

        (
            "Holati",
            {
                "fields": (
                    "is_read",
                    "created_at",
                )
            }
        ),

    )