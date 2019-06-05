from django.http import HttpResponse, HttpResponseRedirect
from .models import Bunk,Person
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
def options(request):
    return render(request,'bunk/options.html')

def all_bunks(request):
    return render(request,'bunk/all_bunks.html',{'all_bunks':Bunk.objects.all()})

def perform_bunks(request):
    try:
        print(request.POST)
        # print(Person.objects.all().pk)
        print( [ i.pk for i in Person.objects.all()])
        selected_bunker = Person.objects.get(pk = request.POST['bunker'])
        selected_bunkee = Person.objects.get(pk = request.POST['bunkee'])

    except (KeyError, Person.DoesNotExist):
            print("except")
            return render(request,'bunk/perform_bunks.html',{'person_set':Person.objects.all()})
    else:
        #selected_choice.votes += 1
        #selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        b = Bunk(bunker = selected_bunker, bunkee = selected_bunkee)
        b.save()
        return HttpResponseRedirect(reverse('options'))

def specific_user(request,key):
    return render(request,'bunk/specific_user.html',{'user':Person.objects.get(pk=key)})
# Create your views here.
