# properties/utils.py
from django.core.cache import cache
from .models import Property

def get_all_properties():
    """Fetch all properties, cached in Redis for 1 hour."""
    properties = cache.get("all_properties")
    if not properties:
        properties = list(Property.objects.all())  # convert queryset to list
        cache.set("all_properties", properties, 3600)  # cache for 1 hour
    return properties
