from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    author = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.title
