
from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin

class UserModel(UserAdmin):
    list_display = ['username','user_type','first_name']
    
admin.site.register(CustomUser,UserModel) 	
admin.site.register(CoursesModel)
admin.site.register(SessionModel)
admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(Staff_Notification)
admin.site.register(Student_Notification)
admin.site.register(Staff_leave)
admin.site.register(Staff_feedback)
admin.site.register(Student_feedback)
admin.site.register(Student_leave)
admin.site.register(Attandance)
admin.site.register(Attandance_report)
admin.site.register(Student_Result)
