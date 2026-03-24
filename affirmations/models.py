from django.db import models

class Affirmation(models.Model):
    text = models.CharField(max_length=255)
