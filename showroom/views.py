from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, render

from .models import Bike


def home(request):
    bikes = Bike.objects.order_by("-featured", "brand", "model")
    paginator = Paginator(bikes, 2)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    featured_bikes = Bike.objects.filter(featured=True)[:3]
    brands = ["Yamaha", "Honda", "KTM", "Royal Enfield", "TVS"]

    return render(
        request,
        "showroom/home.html",
        {
            "page_obj": page_obj,
            "bikes": page_obj.object_list,
            "featured_bikes": featured_bikes,
            "brands": brands,
        },
    )


def bike_detail(request, id):
    bike = get_object_or_404(Bike, id=id)
    return render(request, "showroom/bike_detail.html", {"bike": bike})