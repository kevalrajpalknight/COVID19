from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

# Create your models here.
class Location(models.Model):
    place_name = models.CharField(max_length=256, primary_key=True)
    latitude = models.DecimalField(max_digits=19, decimal_places=16)
    longitude = models.DecimalField(max_digits=19, decimal_places=16)
    
    def __str__(self):
        return str(self.place_name)

class Case(models.Model):
    user = models.ForeignKey(User, related_name = 'Case', on_delete=models.CASCADE, null=True, blank=True)
    address = models.ForeignKey(Location, null = True, blank=True, on_delete=models.CASCADE)
    case_type = models.BooleanField(default=False)   # True is Positive or False is Negative.

    def __str__(self):
        if self.case_type == True:
            return str(self.address) + "- Positive"
        else:
            return str(self.address) + "- Suspect"

    def get_absolute_url(self):
        return reverse('case:all')

    class Meta:
        ordering = ['-case_type']
        unique_together = ['user', 'address']