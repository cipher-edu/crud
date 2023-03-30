from django.db import models
import uuid
# Create your models here.
class Company(models.Model):
    name = models.CharField(max_length=150)
    about = models.CharField(max_length=150)
    logo = models.TextField()
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    def __str__(self):
        return self.name