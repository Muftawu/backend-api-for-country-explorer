from django.db import models

class countries(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)

    def __str__(self):
        return self.name 