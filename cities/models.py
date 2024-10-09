from django.db import models

# Create your models here.
class City(models.Model):
    def __str__(self):
        return self.city_name
    city_name = models.CharField(max_length=200)
    city_population = models.IntegerField(default=0)
    city_province = models.CharField(max_length=200)
    city_area = models.FloatField(default=0)
