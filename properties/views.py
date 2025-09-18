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


@api_view(['GET'])
def property_list(request):
    """Return all properties, cached in Redis for 1 hour."""
    queryset = get_all_properties()
    serializer = PropertySerializer(queryset, many=True)
    return Response(serializer.data)



