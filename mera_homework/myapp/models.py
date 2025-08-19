from django.db import models

class Employee (models.Model):
      name = models.CharField(max_length = 50)
      salary =  models.CharField(max_length = 50)
      designation =  models.CharField(max_length = 50)
      department = models.CharField(max_length=50)
      Qualification = models.CharField(max_length=50)

      def __str__(self):
          return self.name

# Create your models here.
