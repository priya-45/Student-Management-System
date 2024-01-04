from django.shortcuts import render, redirect
from app.models import Staff, Staff_Notification,SessionModel, Staff_leave, Staff_feedback,Attandance,Attandance_report, Subject, SessionModel, Student
from django.contrib import messages
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def HOME(request):
    return render(request, 'Staff/home.html')



@login_required(login_url='/')
def NOTIFICATION(request):
    staff = Staff.objects.filter(admin = request.user.id)
    for i in staff:
        print(i.id)
        staff_id = i.id
        notification = Staff_Notification.objects.filter(staff_id= staff_id)
        context = {
            "notification": notification,
        }
        print(notification)
        return render(request,'Staff/notification.html', context)
    

@login_required(login_url='/')
def STAFF_NOTIFI_MARK_AS_DONE(request, status):
    notification = Staff_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('notification')


@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    leave = Staff.objects.get(admin = request.user.id)
    staff_id = leave.id
    staff_leave_history = Staff_leave.objects.filter(staff_id = staff_id)
    context = {
        'staff_leave_history':staff_leave_history
    }
    return render(request, 'Staff/staff_apply_leave.html', context)
 
@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        date = request.POST['leave_date']
        message = request.POST['leave_message']
        print(request.user)
        staff = Staff.objects.get(admin=request.user.id)


        leave = Staff_leave(
            staff_id = staff,
            data = date,
            message = message

        )
        leave.save()
        messages.success(request, "Leave Successfully Sent !! ")
        return redirect('staff_apply_leave')



def STAFF_FEEDBACK_SEND(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    feedback_history = Staff_feedback.objects.filter(staff_id = staff_id)

    context = {
        'feedback_history' : feedback_history
    }


    return render(request, 'Staff/staff_feedback.html', context)


def STAFF_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST['feedback']
        staff = Staff.objects.get(admin = request.user.id)

        feedback = Staff_feedback(
            staff_id = staff,
            feedback = feedback 
        )
        feedback.save()
        messages.success(request, "Feedback Sended Successfully !!")
        return redirect('staff_feedback')
    


def TAKE_ATTANDANCE(request):
    staff_id  = Staff.objects.get(admin = request.user.id)
    # student = Subject.objects.filter(staff = staff_id)

    subject = Subject.objects.all()
    session = SessionModel.objects.all()
    action = request.GET.get('action')

    students = None 
    get_subject = None
    get_session = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST['subject_id']
            session_id = request.POST['session_id']

            get_subject = Subject.objects.get(id = subject_id)
            get_session = SessionModel.objects.get(id = session_id)

            subject = Subject.objects.filter(id = subject_id)
            for i in subject:
                student_id = i.course.id
                students = Student.objects.filter(course_id =student_id)
                
          

    context = {
        "subject" : subject,
        "session": session,
        'get_subject':get_subject,
        "get_session":get_session,
        'action':action,
        'students':students
    }
    return render(request, 'Staff/take_attandance.html', context)



def STAFF_SAVE_ATTANDANCE(request):
    if request.method == "POST":
        subject_id  = request.POST['subject_id']
        session_id = request.POST['session_id']
        attandance_date = request.POST['attandance_date']
        student_id =request.POST.getlist('student_id')
        
        get_subject = Subject.objects.get(id = subject_id)
        get_session = SessionModel.objects.get(id = session_id)

        attandance = Attandance(
            subject_id = get_subject,
            date = attandance_date,
            session_year = get_session 


        )

        attandance.save()

        for i in student_id:
            int_stud = int(i)
            p_student = Student.objects.get(id = int_stud)
            attandance_report = Attandance_report(
                student_id = p_student,
                attandance_id = attandance

            )
            attandance_report.save()
        print(subject_id, session_id, attandance_date,student_id)
        messages.success(request, "Attandance Taken SuccessFully !!")

    return redirect("take_attandance")



def STAFF_VIEW_ATTANDANCE(request):
    # staff_id = Staff.objects.get(admin = request.user.id)
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
    return render(request, "Staff/view_attandance.html", context)



def STAFF_ADD_RESULT(request):

    staff = Staff.objects.get(admin = request.user.id)

    subjects = Subject.objects.filter(staff_id = staff)
    print(subjects)
    session_year = SessionModel.objects.all()
    action = request.GET.get('action')
    get_subject = None
    get_session = None
    students = None
    if action is not None:
        if request.method == "POST":
           subject_id = request.POST.get('subject_id')
           session_year_id = request.POST.get('session_year_id')

           get_subject = Subject.objects.get(id = subject_id)
           get_session = SessionModel.objects.get(id = session_year_id)

           subjects = Subject.objects.filter(id = subject_id)
           for i in subjects:
               student_id = i.course.id
               students = Student.objects.filter(course_id = student_id)
           


    context = {
        'subjects':subjects,
        'session_year':session_year,
        'action':action,
        'get_subject':get_subject,
        'get_session':get_session,
        'students':students,
    }
    return render(request, 'Staff/add_result.html', context)