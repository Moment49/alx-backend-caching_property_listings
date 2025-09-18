from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import RegisterSerializer, LoginSerializer, PropertySerializer
from .models import Property
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


# properties/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PropertySerializer
from .utils import get_all_properties
from django.http import JsonResponse
from .utils import get_redis_cache_metrics


@api_view(["GET"])
def cache_metrics(request):
    """Return Redis cache hit/miss metrics."""
    metrics = get_redis_cache_metrics()
    return JsonResponse(metrics)

@api_view(['GET'])
@cache_page(60 * 15)  # cache for 15 minutes in Redis
def property_list(request):
    """Return all properties and cache the response for 15 minutes."""
    queryset = get_all_properties()
    serializer = PropertySerializer(queryset, many=True)
    return JsonResponse(serializer.data, safe=False)



