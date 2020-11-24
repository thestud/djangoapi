from django.db import models

# Create your models here.
class Style(models.Model):
    name = models.CharField(max_length=200)
    font = models.CharField(max_length=200)
    fontSize = models.IntegerField()
    backgroundColor = models.CharField(max_length=200)
    fontColor = models.CharField(max_length=200)

    def __str__(self):
        return self.name