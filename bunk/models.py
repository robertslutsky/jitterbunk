from __future__ import unicode_literals

from django.db import models


class Person(models.Model):
    bunks_performed = models.IntegerField(default=0)
    times_bunked_on = models.IntegerField(default=0)
    name = models.CharField(max_length=200)

    def gotBunked(self):
        times_bunked_on+=1

    def performedBunk(self):
        bunks_performed+=1

    def __str__(self):
        return self.name+" performed "+str(self.bunks_performed)+" bunks and has been bunked "+str(self.times_bunked_on)

class Bunk(models.Model):
    bunker_name = models.CharField(max_length=200)
    bunkee_name = models.CharField(max_length=200)
    #bunker = Person.objects.get(name=bunker_name)
    #Person.objects.get(name=bunkee_name).gotBunked()
    def __str__(self):
        return self.bunker_name +" bunked "+self.bunkee_name
# Create your models here.
