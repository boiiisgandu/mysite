from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Myimages(models.Model):
    image = models.ImageField(null=True, blank=True)

    # def __str__(self):
    #     return self.name
    #
    # @property
    # def imageURL(self):
    #     try:
    #         url = self.image.url
    #     except:
    #         url = ''
    #     return url