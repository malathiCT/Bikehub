from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Bike
from .serializers import BikeSerializer


@api_view(["GET"])
def bike_list(request):
    bikes = Bike.objects.order_by("-featured", "brand", "model")
    page_size = int(request.GET.get("page_size", 2))
    page_size = max(1, min(page_size, 10))
    paginator = Paginator(bikes, page_size)
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    data = {
        "count": paginator.count,
        "page": page_obj.number,
        "page_size": page_size,
        "next": None if not page_obj.has_next() else f"?page={page_obj.next_page_number()}&page_size={page_size}",
        "previous": None if not page_obj.has_previous() else f"?page={page_obj.previous_page_number()}&page_size={page_size}",
        "results": BikeSerializer(page_obj.object_list, many=True).data,
    }
    return Response(data)


@api_view(["GET"])
def bike_detail(request, id):
    bike = get_object_or_404(Bike, id=id)
    serializer = BikeSerializer(bike)
    return Response(serializer.data)


@api_view(["POST"])
def bike_create(request):
    serializer = BikeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)

    return Response(serializer.errors, status=400)


@api_view(["PUT"])
def bike_update(request, id):
    bike = get_object_or_404(Bike, id=id)
    serializer = BikeSerializer(bike, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)

    return Response(serializer.errors, status=400)


@api_view(["DELETE"])
def bike_delete(request, id):
    bike = get_object_or_404(Bike, id=id)
    bike.delete()
    return Response({"message": "Bike deleted successfully"}, status=204)