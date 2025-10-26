from django.shortcuts import render

# Create your views here.
def flight_list(request):
    return render(request, 'flights/flight_list.html')
