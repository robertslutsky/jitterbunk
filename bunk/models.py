from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Person(models.Model):
    name = models.CharField(max_length=200)

    def times_bunkee(self):
        return self.bunks_in.count()

    def times_bunker(self):
        return self.bunks_out.count()


    def __str__(self):
        return self.name + " performed " + str(self.times_bunker()) + " bunks and has been bunked "+ str(self.times_bunkee())


class Bunk(models.Model):
    bunker = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='bunks_out')
    bunkee = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='bunks_in')
    time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.bunker.name+" bunked "+self.bunkee.name
# Create your models here.

