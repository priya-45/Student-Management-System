from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from app.models import CoursesModel, SessionModel,Attandance, Attandance_report, CustomUser, Student,Student_feedback,Student_leave ,Staff,Subject, Staff_Notification, Staff_leave,Staff_feedback, Student_Notification
from django.contrib import messages


@login_required(login_url='/')
def HOME(request):
    student = Student.objects.all().count()
    staff = Staff.objects.all().count()
    course = CoursesModel.objects.all().count()
    subject = Subject.objects.all().count()
    student_gender_male = Student.objects.filter(gender = "Male").count()
    student_gender_female = Student.objects.filter(gender = "Female").count()
    print(student_gender_male)
    print(student_gender_female)
    print(student, staff, course,subject)
    context = {
        "student":student,
        'staff':staff,
        'course':course,
        'subject':subject,
        'student_gender_male':student_gender_male,
        'student_gender_female':student_gender_female,
    }
    return render(request,"Hod/hod.html",context)



@login_required(login_url='/')

def ADD_STUDENT(request):
    course = CoursesModel.objects.all()
    session = SessionModel.objects.all()
    if request.method == "POST":
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        gender = request.POST.get('gender')
        course_id = request.POST.get('course_id')
        session_year_id  = request.POST.get('session_year_id')
        print(session_year_id)
        if CustomUser.objects.filter(email = email).exists():
            messages.warning(request, "This email is already taken")
            return redirect("add_student")
        if CustomUser.objects.filter(username = username ).exists():
            messages.warning(request, "This  is already taken")
            return redirect('add_student')
        else:
        
            user = CustomUser(
                first_name = first_name,
                last_name = last_name, 
                email = email,
                username = username,
                profile_pic = profile_pic,
                user_type = 3

                )
            user.set_password(password)
            user.save()

            course = CoursesModel.objects.get(id = course_id)
            session_year = SessionModel.objects.get(id=session_year_id)

            student = Student(
                admin = user,
                address =address,
                session_year_id = session_year,
                course_id = course,
                gender = gender

            )
            student.save()
            messages.success(request, user.first_name + "  " + user.last_name + " Is Added Successfully!")
            return redirect("add_student")

    context ={
        'courses':course,
        'sessions':session
    }
    return render(request,'Hod/add_student.html', context)



# View Student 

@login_required(login_url='/')

def VIEW_STUDENT(request):

    student = Student.objects.all()

    context = {
        'students' : student
    }
    return render(request, 'Hod/view_student.html', context)




# Edit Student 

@login_required(login_url='/')

def EDIT_STUDENT(request, id):
    student = Student.objects.filter(id = id)
    course = CoursesModel.objects.all()
    session = SessionModel.objects.all()

    return render(request, 'Hod/edit_student.html', {'student':student,'course':course,"session":session} )



# Update Student 

@login_required(login_url='/')

def UPDATE_STUDENT(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        profile_pic = request.FILES.get('profile_pic')
        firstName = request.POST['first_name']
        lastName = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        address = request.POST['address']
        password = request.POST['password']
        gender = request.POST['gender']
        course_id = request.POST.get('course_id')
        session_year_id = request.POST['session_year_id']
        user = CustomUser.objects.get(id = student_id)
        user.profile_pic = profile_pic
        user.first_name = firstName
        user.last_name = lastName
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()
     

        student = Student.objects.get(admin = student_id)
        student.address = address
        student.gender = gender

        course = CoursesModel.objects.get(id = course_id)
        student.course_id = course
        print(student.course_id)

        session_year = SessionModel.objects.get(id = session_year_id)
        student.session_year_id = session_year

        student.save()
        messages.success(request,'Record Is Successfully Updated !')
        return redirect('view_student')

    return render(request,'Hod/edit_student.html')



    
        


def DELETE_STUDENT(request, admin):
    student = CustomUser.objects.get(id = admin)
    student.delete()
    messages.error(request,"Student Deleted Successfully !")
    return redirect('view_student')



#  COURSE ADD
@login_required(login_url='/')

def ADD_COURSE(request):
    if request.method == "POST":
        course_name = request.POST['course']
        course = CoursesModel(
            name = course_name
        )
        course.save()
        messages.success(request, "Course Is Created Successfuly! ")
        return redirect("add_course")
    return render(request, 'Hod/add_course.html')


@login_required(login_url='/')

def VIEW_COURSE(request):
    courses = CoursesModel.objects.all()
    return render(request, 'Hod/view_course.html', {'courses': courses})


@login_required(login_url='/')

def EDIT_COURSE(request, id):
    course = CoursesModel.objects.filter(id = id)
    return render(request, 'Hod/edit_course.html', {'course':course})


@login_required(login_url='/')

def UPDATE_COURSE(request):
    if request.method=='POST':
        course_id=request.POST['course_id']
        course_name=request.POST['name']
        course=CoursesModel.objects.get(id=course_id)
        course.name=course_name
        course.save()
        messages.info(request, "Course is Updated Successfully.!")
        return redirect('view_course')
    return render(request, 'Hod/edit_course.html')



@login_required(login_url='/')

def DELETE_COURSE(request, admin):
    course = CoursesModel.objects.get(id = admin)
    course.delete()
    messages.error(request,"Course Deleted Successfully !")
    return redirect('view_course')




@login_required(login_url='/')

def ADD_STAFF(request):
    if request.method == "POST":
        profile_pic = request.FILES['profile_pic']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        address = request.POST['address']
        password = request.POST['password']
        gender = request.POST['gender']
        print(profile_pic,first_name, last_name,email,username,address,password,gender)
        if CustomUser.objects.filter(email = email).exists():
            messages.warning(request,'Email already exists in our database. Please try another one.')
            return redirect('add_staff')
        
        if CustomUser.objects.filter(username = username).exists():
            messages.warning(request,'Usename already exists in our database. Please try another one.')
            return redirect('add_staff')
        
        else:
        
            user = CustomUser(
                first_name = first_name,
                last_name = last_name, 
                email = email,
                username = username,
                profile_pic = profile_pic,
                user_type = 2

                )
            user.set_password(password)
            user.save()


            staff = Staff(
                admin = user,
                address = address,
                gender = gender 
            )


            staff.save()
            messages.success(request, 'Your Staff Added Successfully  !!')
            return redirect('view_staff')
    return render(request, 'Hod/add_staff.html')


    
@login_required(login_url='/')

def VIEW_STAFF(request):
    staffs=Staff.objects.all().order_by('-id')
    context={'staff':staffs}
    return render (request,"Hod/view_staff.html",context)

@login_required(login_url='/')

def EDIT_STAFF(request,id):
    staff =Staff.objects.filter(id=id)
    return render(request, 'Hod/edit_staff.html', {'staff':staff})

@login_required(login_url='/')

def UPDATE_STAFF(request):
    if request.method =='POST':
        staff_id = request.POST['staff_id']
        profile_pic = request.FILES.get('profile_pic')
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        gender = request.POST['gender']
        password = request.POST['password']
        address = request.POST['address']
        print(profile_pic)
       
        user = CustomUser.objects.get(id = staff_id)
        user.profile_pic = profile_pic
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password != None and password != "":
            user.set_password(password)
        if profile_pic != None and profile_pic != "":
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin = staff_id)
        staff.address = address
        staff.gender = gender
        staff.save()

        messages.success(request, "Your Data Updated Successfully !!")
        return redirect('view_staff')
    return render(request, 'Hod/edit_staff.html',)

@login_required(login_url='/')

def DELETE_STAFF(request,admin):
    staff = Staff.objects.filter(id = admin)
    staff.delete()
    messages.error(request,'Data Deleted Successfully!!')
    return redirect ('view_staff')


# Subject
@login_required(login_url='/')

def ADD_SUBJECT(request):
    course_data = CoursesModel.objects.all()
    staff_data = Staff.objects.all()
    if request.method=='POST':
        subject_name=request.POST['subject_name']
        course_id = request.POST['course_id']
        staff_id = request.POST['staff_id']
        course = CoursesModel.objects.get(id = course_id)
        staff = Staff.objects.get(id = staff_id)

        # print(subject_name,course_id,staff_id)
        subj = Subject(subject_name=subject_name,course=course, staff= staff)
        print(subject_name,course_id,staff_id)
        subj.save()
        messages.info(request,"Subject Added Successfully!")
        return redirect("add_subject")
    return render(request, 'Hod/add_subject.html',{"course":course_data, 'staff':staff_data})


@login_required(login_url='/')

def VIEW_SUBJECT(request):
    subjects = Subject.objects.all()
    context =  {'subjs':subjects}
    return render(request, 'Hod/view_subjet.html',context)

    
@login_required(login_url='/')

def EDIT_SUBJECT(request,id):
    subject_id  = Subject.objects.filter(id= id)
    courses = CoursesModel.objects.all()
    staffs = Staff.objects.all()
    return render(request, 'Hod/edit_subject.html',{'subj':subject_id, 'course':courses, 'staff':staffs})

@login_required(login_url='/')

def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_id = request.POST["subject_id"]
        subject_name = request.POST["subject_name"]
        course_id = request.POST["course_id"]
        staff_id = request.POST["staff_id"]

        # course = CoursesModel.objects.get(id = course_id)
        course = CoursesModel.objects.get(id = course_id)

        staff = Staff.objects.get(id = staff_id)

        subject = Subject(
            id = subject_id,
            subject_name = subject_name,
            course = course,
            staff = staff
        )
        subject.save()
        messages.success(request, "Your Data Updated Successfully !!")
        return redirect('view_subject')
    
@login_required(login_url='/')

def DELETE_SUBJECT(request,admin):
    subject = Subject.objects.filter(id = admin)
    print(subject)
    subject.delete()
    messages.error(request,'Data Deleted Successfuly!!')
    return redirect('view_subject')


# Session 
@login_required(login_url='/')

def ADD_SESSION(request):
    if request.method =="POST":
        session_start = request.POST['session_year_start']
        session_end = request.POST['session_year_end']
        session = SessionModel(
            session_start =session_start,
            session_end = session_end
        )
        session.save()
        messages.success(request, 'Your Session Added Successfully !!')
        return redirect('view_session')

    return render(request, 'Hod/add_session.html')


@login_required(login_url='/')

def VIEW_SESSION(request):
    sessions = SessionModel.objects.all()
    return render (request, 'Hod/view_session.html', {"session":sessions})




@login_required(login_url='/')

def EDIT_SESSION(request, id):
    session = SessionModel.objects.filter(id = id)

    return render(request,'Hod/edit_session.html', {"session":session})


@login_required(login_url='/')

def UPDATE_SESSION(request):
    if request.method =='POST':
        session_id = request.POST['session_id']
        session_start = request.POST['session_start']
        session_end = request.POST['session_end']
        print(session_id, session_start, session_end)

        session = SessionModel(
            id = session_id,
            session_start = session_start,
            session_end = session_end
        )
        session.save()
        messages.warning(request, "Session Updated Successfully !!")
        return redirect("view_session")


    return render(request, 'Hod/edit_session.html')


@login_required(login_url='/')

def DELETE_SESSION(request,id):
    session = SessionModel.objects.get(id = id) 
    session.delete()
    messages.error(request,"Session Deleted Successfully !!!")
    return redirect ('view_session')




#  Send Staff Notifications


@login_required(login_url='/')

def STAFF_SEND_NOTIFICATION(request):
    staff  = Staff.objects.all()
    see_notifications = Staff_Notification.objects.all().order_by('-id')[0:5]

    context = {
        "staff":staff,
        "see_notifications":see_notifications
    }
    return render(request, 'Hod/staff_notification.html', context)



@login_required(login_url='/')

def SAVE_STAFF_NOTIFICATION(request):
    if request.method  == "POST":
        staff_id  = request.POST['staff_id']
        messages1 = request.POST['message']

        staff = Staff.objects.get(admin = staff_id)
        notification = Staff_Notification(
            staff_id=staff,
            message=messages1
            )
        notification.save()
        messages.success(request, "Notification Sended Successfully!!")
        return redirect('staff_notification')
    



@login_required(login_url='/')

def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_leave.objects.all()
    context = {
        'leave':staff_leave
    }
    return render(request, 'Hod/staff_leave.html', context)




@login_required(login_url='/')

def STAFF_APPROVE_LEAVE(request,id):
    leave = Staff_leave.objects.get(id = id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')



@login_required(login_url='/')

def STAFF_DISAPPROVE_LEAVE(request,id):
    leave = Staff_leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')



def STAFF_FEEDBACK(request):
    feedbacks = Staff_feedback.objects.all()
    see_feedback= Staff_feedback.objects.all().order_by('-id')[0:5]

    context ={
        'feed' : feedbacks,
        'see_feedback':see_feedback
        }
    return render(request,'Hod/staff_feedback.html',context)


def STAFF_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback_id = request.POST['feedback_id']
        feedback_reply = request.POST['feedback']

        feedback = Staff_feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()
        messages.success(request,"Feedback Replied Successfully")
        return redirect('hod_staff_feedback')

        


#   Send Notification to Student


def STUDENT_SEND_NOTIFICAITON(request):
    student = Student.objects.all()
    notifications = Student_Notification.objects.all()
    context = {
        "student": student,
        "notification":notifications
    }
    return render(request, 'Hod/student_notification.html', context)


def SAVE_STUDENT_NOTIFICATION(request):
    if request.method == 'POST':
        student_id = request.POST['student_id']
        notification = request.POST['message']
        student = Student.objects.get(admin = student_id)
        student_notification = Student_Notification(student_id = student, message = notification )
        student_notification.save()
        messages.info(request, f" Sended Notification To Student Successfuly !!")
        return redirect('student_notification')
 


#  Stundet Feedback 



def STUDENT_FEEDBACK(request):
    feedbacks = Student_feedback.objects.all()
    see_feedback= Student_feedback.objects.all().order_by('-id')[0:5]
    context ={
        "feed":feedbacks, 
        'see_feedback':see_feedback
    }
    return render(request,'Hod/student_feedback.html',context)



def STUDENT_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback_id = request.POST['feedback_id']
        feedback_reply = request.POST['feedback']

        feedback = Student_feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()
        messages.success(request,"Feedback Replied Successfully")
        return redirect('hod_student_feedback')
    


def STUDENT_LEAVE_VIEW(request):
    student_leave = Student_leave.objects.all()
    context = {
        'leave':student_leave
    }
    return render(request, 'Hod/student_leave.html', context)




@login_required(login_url='/')

def STUDENT_APPROVE_LEAVE(request,id):
    leave = Student_leave.objects.get(id = id)
    leave.status = 1
 
    leave.save()
  
    return redirect('student_leave_view')



@login_required(login_url='/')

def STUDENT_DISAPPROVE_LEAVE(request,id):
    leave = Student_leave.objects.get(id = id)
    leave.status = 2
    leave.save()
    return redirect('student_leave_view')



def VIEW_ATTANDANCE(request):
    subject = Subject.objects.all()
    session = SessionModel.objects.all()

    action =request.GET.get('action')
    get_subject = None
    get_session = None
    attandance_date = None
    attandance_report = None
    if action is not None:
        if request.method == "POST":
            subject_id = request.POST['subject_id']
            session_id = request.POST['session_id']
            attandance_date = request.POST['attandance_date']

            get_subject = Subject.objects.get(id = subject_id)
            get_session = SessionModel.objects.get(id = session_id)
            attandance = Attandance.objects.filter(subject_id = get_subject, date = attandance_date)
            print(get_subject)
            for i in attandance:
                attandance_id = i.id
                attandance_report = Attandance_report.objects.filter(attandance_id= attandance_id)
                print(attandance_report)



    context = {
        'subject':subject,
        'session':session,
        'action':action,
        'get_subject':get_subject,
        "get_session":get_session,
        "attandance_date":attandance_date,
        'attandance_report':attandance_report 
    }
    return render(request, 'Hod/view_attandance.html', context)