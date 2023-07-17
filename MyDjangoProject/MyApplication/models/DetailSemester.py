from django.db import models
from django.urls import reverse
import DetailSemester

class Details_Semester(models.Model):
   semester_id = models.CharField(max_length=200)
   plan_id=models.CharField(max_length=200)
   falculty_id=models.CharField(max_length=200)
   semesterName=models.CharField(max_length=255)
   semesterStatus=models.BooleanField(default=True)


   planStatus=models.BooleanField(default=True)
   planYear= models.CharField(max_length=255)
   faculty_name=models.CharFiel(max_length=200)

   def __str__(self):      
       return reverse('book-detail', args=[str(self.id)])
