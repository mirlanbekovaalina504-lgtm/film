from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    duration = models.IntegerField()
    rating = models.FloatField()
    image = models.ImageField(upload_to='movies/', blank=True, null=True)

    def __str__(self):
        return self.title


class Seat(models.Model):
    number = models.CharField(max_length=5)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return self.number


class Booking(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    paid = models.BooleanField(default=False)
