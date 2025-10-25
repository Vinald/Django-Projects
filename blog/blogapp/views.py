from django.shortcuts import render

POSTS = [
    {
        'author': 'John Doe',
        'title': 'First Post',
        'content': 'This is the content of the first post.',
        'date_posted': 'April 20, 2024'
    },
    {
        'author': 'Jane Smith',
        'title': 'Second Post',
        'content': 'This is the content of the second post.',
        'date_posted': 'April 21, 2024'
    },
    {
        'author': 'Alice Johnson',
        'title': 'Third Post',
        'content': 'This is the content of the third post.',
        'date_posted': 'April 22, 2024'
    }
]

def home(request):
    return render(request, 'blog/home.html')


def about(request):
    return render(request, 'blog/about.html')