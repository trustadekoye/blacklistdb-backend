from django.db import models


class ScammersList(models.Model):
    STATUS_CHOICES = (
        ("pending", "Pending Review"),
        ("approved", "Approved"),
        ("rejected", "Rejected"),
    )

    reporters_name = models.CharField(max_length=100, blank=True)
    reporters_email = models.CharField(max_length=100, blank=True)
    reporter_phone = models.CharField(max_length=20, blank=True)

    scammers_name = models.CharField(max_length=100, blank=True)
    business_name = models.CharField(max_length=100, blank=True)
    scammers_account = models.CharField(max_length=100, blank=True)
    scammers_bank = models.CharField(max_length=100, blank=True)
    scammers_phone = models.CharField(max_length=20, blank=True)
    scammers_instagram = models.CharField(max_length=100, blank=True)
    scammers_twitter = models.CharField(max_length=100, blank=True)
    date_occurred = models.DateTimeField()
    description = models.TextField(blank=True)
    scammers_image = models.URLField(max_length=500, blank=True)
    other_documents = models.URLField(max_length=500, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")

    def __str__(self):
        return f"{self.scammers_name} - {self.status}"

    class Meta:
        verbose_name = "Scammer"
        verbose_name_plural = "Scammers"
        ordering = ["-date_occurred"]
