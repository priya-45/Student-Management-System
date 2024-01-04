"""
URL configuration for student_management_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views, Hod_views, Staff_views, Student_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name="Base"),

    #  Login Path 
    path('', views.LOGIN,name="login"),
    path('dologin/', views.doLogin, name="dologin"),
    path("logout/", views.LOGOUT, name ="logout" ),

    # Profile Path

    path('profile', views.PROFILE, name = 'profile'),
    path("profile/update", views.PROFILE_UPDATE, name='profile_update'),

    # Hod path

    path('hod/home', Hod_views.HOME, name= 'hod_Home'),
    path('hod/student/add',Hod_views.ADD_STUDENT, name ='add_student' ),
    path('hod/student/view', Hod_views.VIEW_STUDENT, name='view_student'),
    path('hod/student/edit/<int:id>',Hod_views.EDIT_STUDENT, name='edit_student'),
    path('hod/student/update', Hod_views.UPDATE_STUDENT, name='update_student'),
    path('hod/student/delete/<int:admin>', Hod_views.DELETE_STUDENT, name='delete_student'),



#  Course
    path('hod/course/add', Hod_views.ADD_COURSE, name='add_course'),
    path('hod/course/view', Hod_views.VIEW_COURSE, name='view_course'),
    path('hod/course/edit/<int:id>', Hod_views.EDIT_COURSE, name='edit_course'),
    path('hod/course/update', Hod_views.UPDATE_COURSE, name='update_course'),
    path('hod/course/delete/<int:admin>', Hod_views.DELETE_COURSE, name='delete_course'),


#  Staff
     
    path('hod/staff/add', Hod_views.ADD_STAFF , name = 'add_staff'),
    path('hod/staff/view', Hod_views.VIEW_STAFF, name='view_staff'),
    path('hod/staff/edit/<int:id>', Hod_views.EDIT_STAFF, name='edit_staff'),
    path('hod/staff/update', Hod_views.UPDATE_STAFF, name='update_staff'),
    path('hod/staff/delete/<int:admin>', Hod_views.DELETE_STAFF, name='delete_staff'),

# Subject
    path('hod/subject/add',Hod_views.ADD_SUBJECT, name='add_subject'),
    path('hod/subject/view',Hod_views.VIEW_SUBJECT,name='view_subject'),
    path('hod/subject/edit/<int:id>',Hod_views.EDIT_SUBJECT,name='edit_subject'),
    path("hod/subject/update", Hod_views.UPDATE_SUBJECT, name= 'update_subject'),
    path('hod/subject/delete/<int:admin>', Hod_views.DELETE_SUBJECT, name='delete_subject'),


# Session

    path('hod/session/add/', Hod_views.ADD_SESSION,name='add_session'),
    path("hod/session/view",Hod_views.VIEW_SESSION, name='view_session'),
    path('hod/session/edit/<int:id>', Hod_views.EDIT_SESSION, name= 'edit_session'),
    path("hod/session/update",Hod_views.UPDATE_SESSION, name="update_session"),
    path('hod/session/delete/<int:id>', Hod_views.DELETE_SESSION, name='delete_session'),
    


    #  Send Notifications

    path('hod/staff/notification', Hod_views.STAFF_SEND_NOTIFICATION, name='staff_notification'),
    path('hod/staff/save_notification', Hod_views.SAVE_STAFF_NOTIFICATION, name='save_notification'),
    
    path('hod/student/notification', Hod_views.STUDENT_SEND_NOTIFICAITON, name = 'student_notification'),
    path('hod/student/save_notification', Hod_views.SAVE_STUDENT_NOTIFICATION, name='save_student_notification'),

    

    # Staff Leave 
    path('hod/staff/leave_view', Hod_views.STAFF_LEAVE_VIEW, name = 'staff_leave_view'),
    path('hod/staff/approve_leave/<int:id>', Hod_views.STAFF_APPROVE_LEAVE, name = 'staff_approve_leave'),   
    path('hod/staff/disapprove_leave/<int:id>', Hod_views.STAFF_DISAPPROVE_LEAVE, name = 'staff_disapprove_leave'),   
    path('hod/staff_reply_feedback', Hod_views.STAFF_FEEDBACK, name = "hod_staff_feedback"),
    path('hod/staff_reply_feedback_save', Hod_views.STAFF_FEEDBACK_SAVE, name = "hod_staff_feedback_save"),


    #  Student Leave
    path('hod/student/leave_view', Hod_views.STUDENT_LEAVE_VIEW, name = 'student_leave_view'),
    path('hod/student/approve_leave/<int:id>', Hod_views.STUDENT_APPROVE_LEAVE, name = 'student_approve_leave'),   
    path('hod/student/disapprove_leave/<int:id>', Hod_views.STUDENT_DISAPPROVE_LEAVE, name = 'student_disapprove_leave'),   

    




    #  Reply Student Feedback

    path('hod/student_reply_feedback', Hod_views.STUDENT_FEEDBACK, name = 'hod_student_feedback'),
    path('hod/student_reply_save', Hod_views.STUDENT_FEEDBACK_SAVE, name='hod_student_feedback_save'),

    # view attandance 

    path('hod/view_attandance', Hod_views.VIEW_ATTANDANCE, name = 'hod_view_attandance'),
    #  Staff Feedback 

    path('staff/feedback', Staff_views.STAFF_FEEDBACK_SEND, name = 'staff_feedback'),
    path("staff/feedback_save", Staff_views.STAFF_FEEDBACK_SAVE, name='staff_feedback_save'),

    #  This is Staff Panlel

    path("staff/home/", Staff_views.HOME, name='home'),
    path('staff/notification',Staff_views.NOTIFICATION , name="notification"),
    path('staff/mark_as_done/<str:status>', Staff_views.STAFF_NOTIFI_MARK_AS_DONE, name='mark_as_done'),
    path('staff/apply_leave', Staff_views.STAFF_APPLY_LEAVE, name='staff_apply_leave'),
    path('staff/apply_leave_save', Staff_views.STAFF_APPLY_LEAVE_SAVE, name='staff_leave_save'),
    
    #  Take Attandance

    path('staff/take_attandance', Staff_views.TAKE_ATTANDANCE, name = 'take_attandance'),
    path('staff/save/sttandance',Staff_views.STAFF_SAVE_ATTANDANCE, name = 'staff_save_attandance'),
    path('staff/view_attandance', Staff_views.STAFF_VIEW_ATTANDANCE, name = "staff_view_attandance"),
    
    # add result 

    path('staff/add/result',Staff_views.STAFF_ADD_RESULT, name = 'add_result'),


         
    
    #  Student Panel

    path('student/home', Student_views.Home, name = 'student_home'),
    path("student/notification", Student_views.STUDENT_NOTIFICATION, name = 'stud_notification'),
    path('student/mark_as_done/<str:status>', Student_views.STUDENT_NOTIFI_MARK_AS_DONE, name='stud_mark_as_done'),

    #  Student Feedback

    path('student/feedback', Student_views.STUDENT_FEEDBACK_SEND, name = 'student_feedback'),
    path('student/feedback_save', Student_views.STUDENT_FEEDBACK_SAVE, name = "student_feedback_save"),


    # Student Leave

    path('student/apply_leave', Student_views.STUDENT_APPLY_LEAVE, name='student_apply_leave'),
    path('student/leave_save', Student_views.STAFF_APPLY_LEAVE_SAVE, name = "student_leave_save"),


    # View Attandance

    path('student/view_attandance', Student_views.STUDENT_VIEW_ATTANDANCE, name='view_attandance')
    








]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)
