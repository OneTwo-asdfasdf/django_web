from django.db import models
from django.utils import timezone

# Create your models here.
class Anounce(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    context = models.TextField()
    created = models.DateTimeField(default = timezone.now)
    published = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published = timezone.now()
        self.save()


    def __unicode__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created = models.DateTimeField(default = timezone.now)

    def publish(self):
        self.created = timezone.now()
        self.save()

    def __unicode__(self):
        return self.name
