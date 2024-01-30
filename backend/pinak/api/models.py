from django.db import models
from django.contrib.auth.models import User

class DataModel(models.Model):
    CATEGORY = (
    ('Books', 'Books'),
    ('Magazine', 'Magazine'),
    ('Movie', 'Movie'),
    )
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    author = models.CharField(max_length=3000)
    category = models.CharField(max_length=30, choices=CATEGORY)
    releaseDate = models.CharField(max_length=100)
    image = models.ImageField(upload_to='photos/products', blank=True)
    
    
user = models.OneToOneField(User, on_delete=models.CASCADE)
