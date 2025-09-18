from django.db import models

# Create your models here.
class Property(models.Model):
    title = models.CharField(max_length=200, blank=False, null=True)
    description = models.TextField(blank=False, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    location = models.CharField(max_length=200, blank=False, null=False)
    created_at = models.DateTimeField(auto_now_add=True)    

    def __str__(self):
        return f"This is the propery: {self.title} located at {self.location} priced at {self.price}"
    