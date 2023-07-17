from django.db import models
from django.urls import reverse
import uuid
import Classroom

class Classroom(models.Model):
    classroom_id = models.UUIDField()
    student = models.ForingKey(Student,student_id)
    teacher = models.ForingKey(Teacher,teacher_id)
    course = models.ForingKey(Course,course_id)
    capacidad = models.IntegerField()
    Num_Classroom = models.CharField(max_length=255)
    Classroom_active = models.BooleanField(default=True)    
    
    class Meta:
	    verbose_name_plural = 'Classroom'
        ordering = ('-created',)
    def __str__(self):
	    return self.title
	 
    
	