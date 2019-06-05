from django.http import HttpResponse
from .models import Bunk,Person
from django.shortcuts import get_object_or_404, render
def options(request):
    return render(request,'bunk/options.html')

def all_bunks(request):
    return render(request,'bunk/all_bunks.html',{'all_bunks':Bunk.objects.all()})

def perform_bunks(request):
    return render(request,'bunk/perform_bunks.html',{'person_set':Person.objects.all()})
# Create your views here.
