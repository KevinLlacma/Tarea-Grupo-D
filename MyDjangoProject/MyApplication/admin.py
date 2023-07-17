from django.contrib import admin
from .models.Assignment import Assignment 
from .models.Classroom import Classroom 
from .models.Course import Course 
from .models.DetailSemester import DetailSemester
from .models.Enroll import Enroll
from .models.Group import Group 
from .models.School import School
from .models.Semester import Semester
from .models.User_Type import User_Type
from .models.User import User  
# Register your models here.

admin.site.register(Assignment)
admin.site.register(Classroom)
admin.site.register(DetailSemester)
admin.site.register(Course)
admin.site.register(Enroll)
admin.site.register(Group)
admin.site.register(School)
admin.site.register(Semester)
admin.site.register(User_Type)
admin.site.register(User)