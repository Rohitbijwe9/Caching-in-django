from django.db import models

class Fruits(models.Model):
    fname=models.CharField(max_length=30)

    def __str__(self):
        return self.fname