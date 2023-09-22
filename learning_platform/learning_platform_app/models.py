from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Access(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)


class Lesson(models.Model):
    name = models.CharField(max_length=255)
    video_link = models.URLField()
    duration_seconds = models.PositiveIntegerField()


class LessonView(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    view_time_seconds = models.PositiveIntegerField()
    status = models.BooleanField(default=False)
