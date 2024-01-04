from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    User = (
        (1,'HOD'),
        (2,'STAFF'),
        (3,'STUDENT')
    ) 
    user_type=models.CharField(choices=User, max_length=200,default='1')

    profile_pic = models.ImageField(upload_to='media/profile_pic')
    
# Create your models here.


class CoursesModel(models.Model):
    name = models.CharField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateField(auto_now_add= True)

    def __str__(self):
        return self.name
    

class SessionModel(models.Model):
    session_start =models.CharField(max_length=100)
    session_end = models.CharField(max_length=100)

    def __str__(self):
        return self.session_start + " To "  + self.session_end


class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length = 50)
    course_id = models.ForeignKey(CoursesModel, on_delete=models.DO_NOTHING)
    session_year_id = models.ForeignKey(SessionModel, on_delete =  models.DO_NOTHING)
    createdAt = models.DateTimeField(auto_now_add=True)
    uodatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    


class Staff(models.Model):
    admin = models.OneToOneField(CustomUser , on_delete=models.CASCADE )
    address = models.TextField()
    gender = models.CharField(max_length = 40)
    createdAt = models.DateTimeField(auto_now_add = True )
    updatedAt =  models.DateTimeField(auto_now_add = True )


    def __str__(self) :
        return self.admin.username


class Subject(models.Model):
    subject_name = models.CharField(max_length=200)
    course = models.ForeignKey(CoursesModel,on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add = True, null=True)
    updatedAt = models.DateTimeField(auto_now = True)



    def __str__(self) :
        return self.subject_name
    


class Staff_Notification(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.staff_id.admin.first_name+" "+self.staff_id.admin.last_name
    


class Student_Notification(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    message = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(default=0, null=True)

    def __str__(self):
        return self.student_id.admin.first_name 
    

class Staff_leave(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    message  = models.TextField()
    status = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + "  " + self.staff_id.admin.last_name
    


class Staff_feedback(models.Model):
    staff_id = models.ForeignKey(Staff, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.staff_id.admin.first_name + " " + self.staff_id.admin.last_name
        



class Student_feedback(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    feedback = models.TextField()
    feedback_reply = models.TextField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id.admin.first_name + " " + self.student_id.admin.last_name
    



class Student_leave(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    data = models.CharField(max_length=100)
    message  = models.TextField()
    status = models.IntegerField(default=0)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_id.admin.first_name + "  " + self.student_id.admin.last_name
    

class Attandance(models.Model):
    subject_id = models.ForeignKey(Subject, on_delete=models.DO_NOTHING)
    date = models.DateField()
    session_year = models.ForeignKey(SessionModel, on_delete=models.DO_NOTHING)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now= True)

    def __str__(self) -> str:
        return self.subject_id.subject_name 
    

class Attandance_report(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.DO_NOTHING)
    attandance_id = models.ForeignKey(Attandance, models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.student_id.admin.first_name
    


class Student_Result(models.Model):
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    assignmentt_mark = models.IntegerField()
    exam_mark = models.IntegerField()
    createdAt = models.DateField(auto_now_add=True)
    updatedAt = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.student_id.admin.first_name
