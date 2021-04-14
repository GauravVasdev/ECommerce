from django.db import models

# Create your models here.
from django.db import models
# Create your models here.
class PersonData(models.Model):
    C_Name=models.CharField(max_length=255)
    C_EmailID=models.CharField(max_length=255)
    C_Password=models.CharField(max_length=255)

