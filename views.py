from .models import *
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from enrollments.models import *
# Create your views here.

@login_required(login_url="loginpage")
def profile(request):
        if request.user.user_type == False :
            doctor=Doctor.objects.get(doc_id=request.user.id)
            context = {
            'basic': doctor,
            }
        else:
            student=Student.objects.get(stu_id=request.user.id)
            print(student)
            id=student.stu_id_id
            print(id)
            stu_info=Student_info.objects.get(student_id_id=id)
            print(stu_info)
            context = {
            'basic': student,
            "dynamic":stu_info
            }
  
        return render(request,'profile/profile.html',context)