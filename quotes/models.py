from djongo import models
from .connect import get_mongodb


connection = get_mongodb()

class Tag(models.Model):
    id = models.ObjectIdField()
    name = models.CharField(max_length=50)

class Author(models.Model):
    _id = models.ObjectIdField()
    fullname = models.CharField(max_length=255)
    born_date = models.CharField(max_length=50)
    born_location = models.CharField(max_length=255)
    description = models.TextField()

class Quote(models.Model):
    _id = models.ObjectIdField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ArrayField(model_container=Tag)
    quote = models.TextField()
