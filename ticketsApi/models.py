from django.db import models

# Guest movie reservation

class Guest(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return self.name
class Movie(models.Model):
    hall = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    date = models.DateField()

    def __str__(self):
        return self.name


class Reservations(models.Model):
    guest = models.ForeignKey(Guest,related_name="reservation",on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie,related_name="reservation",on_delete=models.CASCADE)

    

