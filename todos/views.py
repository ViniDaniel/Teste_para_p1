from django.shortcuts import render

def index(request):
    return render(request, 'todos/index.html')

# Create your views here.
