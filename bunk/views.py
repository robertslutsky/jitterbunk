from django.http import HttpResponse


def options(request):
    return HttpResponse("Hello, world. You're at the bunk index.")

# Create your views here.
