from django.contrib import admin
from .models import ScammersList

admin.site.register(ScammersList)


class ScammersListAdmin(admin.ModelAdmin):
    list_display = (
        "scammers_name",
        "business_name",
        "scammers_bank",
        "scammers_account",
        "date_occurred",
        "status",
        "created_at",
    )
    list_filter = ("status", "date_occurred", "created_at")
    search_fields = (
        "scammers_name",
        "scammers_account",
        "scammers_phone",
        "scammers_instagram",
        "scammers_twitter",
    )
    readonly_fields = ["created_at"]
    list_editable = ["status"]

    actions = ["approve_reports", "reject_reports"]

    def approve_reports(self, request, queryset):
        queryset.update(status="approved")

    approve_reports.short_description = "Approve selected Reports"

    def reject_reports(self, request, queryset):
        queryset.update(status="rejected")

    reject_reports.short_description = "Reject selected Reports"

    fieldsets = (
        (
            "Reporter Information",
            {"fields": ("reporters_name", "reporters_email", "reporter_phone")},
        ),
        (
            "Scammer Information",
            {
                "fields": (
                    "scammers_name",
                    "scammers_account",
                    "scammers_bank",
                    "scammers_phone",
                    "scammers_instagram",
                    "scammers_twitter",
                )
            },
        ),
        ("Incident Details", {"fields": ("date_occurred", "description")}),
        ("Evidence", {"fields": ("scammers_image", "other_documents")}),
    )
