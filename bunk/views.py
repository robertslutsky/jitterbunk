from django.http import HttpResponse, HttpResponseRedirect
from .models import Bunk,Person
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.utils import timezone

def bunk_options(request):
    return render(request,'bunk/bunk_options.html')

def all_bunks(request):
    return render(request,'bunk/all_bunks.html',{'all_bunks':Bunk.objects.all()})

def perform_bunks(request):
    if request.method == 'POST':
        try:
            # These can generate ValueError or KeyError
            bunker_pk = int(request.POST['bunker'])
            bunkee_pk = int(request.POST['bunkee'])

            # These can generate Person.DoesNotExist
            selected_bunker = Person.objects.get(pk=bunker_pk)
            selected_bunkee = Person.objects.get(pk=bunkee_pk)
        except (ValueError, KeyError, Person.DoesNotExist):
            return render(request, 'bunk/perform_bunks.html', {
                'person_set': Person.objects.all()
            })
        else:
            b = Bunk(bunker=selected_bunker, bunkee=selected_bunkee)
            b.save()
            return HttpResponseRedirect(reverse('bunk_options'))
    else:
        return render(request, 'bunk/perform_bunks.html', {
            'person_set': Person.objects.all()
        })


def specific_user(request, key):
    print(key)
    print([i.pk for i in Person.objects.all()])
    user = get_object_or_404(Person, pk=key)
    return render(request,'bunk/specific_user.html', {
        'user':user
    })
def home(request):
    return render(request,'home.html')
