from django.db import models


class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    departure = models.CharField(max_length=100)
    arrival = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    duration = models.IntegerField()

    def __str__(self):
        return f"{self.flight_number}: {self.departure} to {self.arrival}"