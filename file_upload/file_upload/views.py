from django.shortcuts import render
from django.http import HttpResponse
import sys, os
UPLOADE_DIR = os.path.dirname(os.path.dirname(__file__)) + '/static/files/'

def index(request):
    if request.method == 'POST':
        file = request.FILES['file']
        path = os.path.join(UPLOADE_DIR, file.name)
        destination = open(path, 'wb')

        for chunk in file.chunks():
            destination.write(chunk)

    return render(request, 'index.html')
