from django.db import models

# Create your models here.
class Testimonical(models.Model):
    image=models.ImageField(upload_to='pics')
    heading=models.CharField(max_length=250)
    description=models.TextField()
    def __str__(self):
        return self.heading

class Ceo(models.Model):
    image = models.ImageField(upload_to='pics')
    heading = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.heading


class Manager(models.Model):
    image = models.ImageField(upload_to='pics')
    heading = models.CharField(max_length=250)
    description = models.TextField()

    def __str__(self):
        return self.heading

class Background(models.Model):
    image=models.ImageField(upload_to='pics')

    def __image__(self):
        return self.image