import hashlib

from django.db import models


class Bike(models.Model):
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    engine_capacity = models.CharField(max_length=50, default="150cc")
    mileage = models.CharField(max_length=50, default="45 km/l")
    description = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    color = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return f"{self.brand} {self.model}"

    def get_display_image_url(self):
        if self.image_url:
            return self.image_url

        fallback_images = [
            "https://images.unsplash.com/photo-1511994298241-608e28f14fde?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=900&q=80",
            "https://images.unsplash.com/photo-1517524206127-48bbd363f3d7?auto=format&fit=crop&w=900&q=80",
        ]

        seed = str(self.pk or f"{self.brand}-{self.model}-{self.color}")
        digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
        index = int(digest[:2], 16) % len(fallback_images)
        return fallback_images[index]