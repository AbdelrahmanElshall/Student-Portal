from django.db import models
from django.db.models.base import Model
from enrollments.models import *
# Create your models here.

class Student_info(models.Model):
    student_id = models.ForeignKey(Student,on_delete=models.CASCADE)
    gpa=models.DecimalField(max_digits=5,decimal_places=4)
    hours=models.IntegerField()
    level=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.gpa} -- {self.hours}"

    class Meta():
        ordering=['gpa']
    