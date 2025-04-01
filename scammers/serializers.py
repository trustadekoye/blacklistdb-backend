from rest_framework import serializers
from .models import ScammersList


class ScammersListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ScammersList
        fields = "__all__"
        read_only_fields = ("created_at", "status")
