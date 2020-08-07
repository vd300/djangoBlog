from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse                 #reverse returns the full pathh of url as string compared to redirect.

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):                                   #ImproperlyConfigured at /post/new/||No URL to redirect to.  Either provide a url or define a get_absolute_url method on the Model.
        return reverse('post-detail', kwargs={'pk': self.pk})
