from django.db import models

# Create your models here.\

class ModelTable(models.Model):
    first_name =  models.CharField(max_length=255)
    last_name =  models.CharField(max_length=255)
    reg_no =  models.CharField(max_length=255)
    cource =  models.CharField(max_length=255)
    topic =  models.TextField()

    def __str__(self):
        return self.first_name
