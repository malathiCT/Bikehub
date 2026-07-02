from rest_framework import serializers

from .models import Bike


class BikeSerializer(serializers.ModelSerializer):
    display_image_url = serializers.SerializerMethodField()

    class Meta:
        model = Bike
        fields = "__all__"

    def get_display_image_url(self, obj):
        return obj.get_display_image_url()