from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    userid = models.CharField(max_length=20)
    token = models.CharField(max_length=60)
    friends = models.CharField(max_length=500)
    # def __str__(self):
    #     return '%s: %s' % (self.author, self.textOfStatement)

