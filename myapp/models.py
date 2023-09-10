from django.db import models

# Create your models here.


class Image(models.Model):
    prod_name = models.CharField(max_length=150, null=False, default=None)
    photo = models.ImageField(upload_to="myimage")
    date = models.DateTimeField(auto_now_add=True)
    up_file = models.FileField(upload_to="myfile", default=None)
