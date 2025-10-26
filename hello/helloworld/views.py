from django.shortcuts import render

def hello_world(request):
    return render(request, 'hello/helloworld.html')

def greet(request, name: str):
    return render(request, 'hello/greet.html', {'name': name})
