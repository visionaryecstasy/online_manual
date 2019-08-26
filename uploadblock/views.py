from django.shortcuts import render
from . import models

# Create your views here.
def upload(request):
    file = models.file.objects.all()
    return render(request, 'uploadblock/show_files.html', {'file': file})