from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.
class SkyColor(models.Model):
    SKY_COLOR = [
        ("BL", "BLUE"),
        ("YE", "YELLOW"),
        ("RE", "RED"),
        ("OR", "ORANGE"),
        ("PI", "PINK"),
    ]
    color = models.CharField(max_length=50)
    image = models.ImageField(upload_to="skys/")
    date_added = models.DateTimeField(default=timezone.now)
    # date_added = models.TimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=SKY_COLOR)
    description = models.TextField(default="")
    # time = models.TimeField()

    def __str__(self):
        return self.color


# One to Many


class SkyReview(models.Model):
    skyColor = models.ForeignKey(
        SkyColor, on_delete=models.CASCADE, related_name="review"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.ImageField()
    comment = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} review for {self.sky.name}"


# Many to Many
class Season(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    sky_varieties = models.ManyToManyField(SkyColor, related_name="season")

    def __str__(self):
        return self.name


# one to one
class PhotoCertificate(models.Model):
    sky = models.OneToOneField(
        SkyColor, on_delete=models.CASCADE, related_name="cetificate"
    )
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f"Cetificate for photo of {self.sky.name}"
