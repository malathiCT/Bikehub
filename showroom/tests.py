from django.test import TestCase
from django.urls import reverse

from .models import Bike


class BikeShowroomTests(TestCase):
    def setUp(self):
        Bike.objects.create(
            brand="Yamaha",
            model="R15 V4",
            price="199000.00",
            engine_capacity="155cc",
            mileage="45 km/l",
            description="A sporty street bike crafted for sharp acceleration.",
            image_url="https://images.unsplash.com/photo-1558981806-ec527fa84c39?auto=format&fit=crop&w=900&q=80",
            featured=True,
        )

    def test_home_page_renders(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Book Test Ride")

    def test_api_bikes_list_returns_paginated_data(self):
        response = self.client.get(reverse("bike-list"), {"page": 1, "page_size": 1})
        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn("results", payload)

    def test_distinct_bikes_get_unique_fallback_images(self):
        yamaha = Bike.objects.create(
            brand="Yamaha",
            model="R15",
            price="180000.00",
            engine_capacity="155cc",
            mileage="45 km/l",
            description="A sharp performer.",
            image_url="",
        )
        honda = Bike.objects.create(
            brand="Honda",
            model="CBR 250R",
            price="220000.00",
            engine_capacity="249cc",
            mileage="35 km/l",
            description="A premium commuter with style.",
            image_url="",
        )

        self.assertNotEqual(yamaha.get_display_image_url(), honda.get_display_image_url())
