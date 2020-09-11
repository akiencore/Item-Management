from django.db import models

# Create your models here.
class Container(models.Model):
    name = models.CharField(unique=True, blank=False, null=False, max_length=50)

    length = models.CharField(blank=True, null=False, max_length=10)
    width = models.CharField(blank=True, null=False, max_length=10)
    height = models.CharField(blank=True, null=False, max_length=10)

    color = models.CharField(blank=False, null=False, max_length=20)

    purpose = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    # Container.objects.create(name='shelf', length = '0.6m', width = '0.35m', height = '2m', color = 'black')


class Item(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50)

    length = models.CharField(blank=True, null=False, max_length=10)
    width = models.CharField(blank=True, null=False, max_length=10)
    height = models.CharField(blank=True, null=False, max_length=10)
    
    color = models.CharField(blank=False, null=False, max_length=20)
    category = models.CharField(blank=True, null=False, max_length=20)
    
    in_container = models.IntegerField(blank=False, null=False)
    purpose = models.TextField(blank=True, null=True)
    note = models.TextField(blank=True, null=True)

    # Item.objects.create(name='book', length = '25cm', width = '0.18cm', height = '0.6cm', color = 'brown', category = 'book', in_container = 1)