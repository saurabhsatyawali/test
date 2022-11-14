from django.db import models
from datetime import date
class AuthorManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(name='saurabh')

class Book(models.Model):
    name=models.CharField(max_length=79)
    au=models.ForeignKey('Author',on_delete=models.CASCADE,related_name="%(app_label)s_%(class)s")


class Author(models.Model):
    name=models.CharField(max_length=79)
    ob=AuthorManager()
    objects=models.Manager()