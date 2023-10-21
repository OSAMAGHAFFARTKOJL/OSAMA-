# calculator/models.py
from django.db import models

class Calculation(models.Model):
    expression = models.CharField(max_length=200)
    result = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
