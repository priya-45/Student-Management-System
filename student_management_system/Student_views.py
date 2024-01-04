from django.shortcuts import render, redirect
from app.models import Student_Notification, Student, Student_feedback, Student_leave, Subject, Attandance, Attandance_report
from django.contrib import messages

def Home(request):
    return render(request, 'Student/home.html')



def STUDENT_NOTIFICATION(request):
    student = Student.objects.get(admin = request.user.id)
    student_id = student.id
    notifications = Student_Notification.objects.filter(student_id = student_id)
    context = {
        'notification' : notifications
    }
    print(notifications)


    print(student)
    
    return render(request, 'Student/notification.html', context)




def STUDENT_NOTIFI_MARK_AS_DONE(request, status):
    notification = Student_Notification.objects.get(id = status)
    notification.status = 1
    notification.save()
    return redirect('stud_notification')


def STUDENT_FEEDBACK_SEND(request):
    student_id = Student.objects.get(admin=request.user.id)
    feedback_history = Student_feedback.objects.filter(student_id = student_id)

    context = {
        'feedback_history' : feedback_history
    }

    return render(request, 'Student/student_feedback.html', context)


def STUDENT_FEEDBACK_SAVE(request):
    if request.method == "POST":
        feedback = request.POST['feedback']
        student = Student.objects.get(admin = request.user.id)
        print(feedback)

        feedback = Student_feedback(
            student_id = student,
            feedback = feedback 
        )
        feedback.save()
        messages.success(request, "Feedback Sended Successfully !!")
        return redirect('student_feedback')
    

def STUDENT_APPLY_LEAVE(request):
    leave = Student.objects.get(admin = request.user.id)
    student_id = leave.id
    student_leave_history = Student_leave.objects.filter(student_id = student_id)
    context = {
        'student_leave_history':student_leave_history
    }
    return render(request, 'Student/student_apply_leave.html', context)



def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == "POST":
        date = request.POST['leave_date']
        message = request.POST['leave_message']
        print(date, message)
        print(request.user)
        student = Student.objects.get(admin=request.user.id)
        leave = Student_leave(
            student_id = student,
            data = date,
            message = message

        )
        leave.save()
        messages.success(request, "Leave Successfully Sent !! ")
        return redirect('student_apply_leave')
    

def STUDENT_VIEW_ATTANDANCE(request):
    student = Student.objects.get(admin = request.user.id)
    subjects = Subject.objects.filter(course  = student.course_id)
    get_subject= None
    attandance_report = None
    actions = request.GET.get('action')
    if actions is not None:
        if request.method == "POST":
            subject_id = request.POST['subject_id']
            get_subject = Subject.objects.get(id = subject_id)

            attandance = Attandance.objects.get(subject_id = get_subject)
            attandance_report = Attandance_report.objects.filter(student_id =student, attandance_id__subject_id= subject_id)

            print(subject_id)


    context = {
        'subject':subjects,
        'action':actions,
        'get_subject':get_subject, 
        "attandance_report":attandance_report

    }

    print(subjects)
    return render(request, 'Student/view_attandance.html', context)