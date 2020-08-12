from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=200)
    kcalorie = models.FloatField()
    carbs = models.FloatField()
    fat = models.FloatField()
    protein = models.FloatField()
    sodium = models.FloatField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"pk": self.pk})
    