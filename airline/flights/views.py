from django.shortcuts import render
from .models import Flight


# Create your views here.
def flight_list(request):
    return render(request, 'flights/flight_list.html', {
        'flights': Flight.objects.all()
    , 'title': 'Flight List'})


def flight_details(request, flight_id):
    flight = Flight.objects.get(id=flight_id)
    return render(request, 'flights/flight_details.html', {
        'flight': flight,
        'title': f'Flight {flight.flight_number} Details'
    })