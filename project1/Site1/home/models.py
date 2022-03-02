from django.contrib.auth.models import User
from django.db import models
import uuid

class Bil(models.Model):
    name = models.CharField(max_length=100)
    ip = models.GenericIPAddressField(null=True)


class Filee(models.Model):
    bil = models.OneToOneField(
        Bil,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=100)
    file = models.FileField(null=True)


class VisitHis(models.Model):
    name = models.CharField(max_length=10)


# Elasticsearch

class Car(models.Model):
    name = models.CharField(max_length=100)
    color = models.CharField(max_length=100)
    description = models.TextField()
    type = models.IntegerField(choices=[
        (1, "Sedan"),
        (2, "Truck"),
        (3, "SUV"),
    ])



