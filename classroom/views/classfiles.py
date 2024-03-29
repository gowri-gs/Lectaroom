from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib import messages
from classroom.models import ClassRoom, MemberShip, ClassFiles
from profiles.models import Teacher, Student
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class ClassFilesView(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request,id):
        room = get_object_or_404(ClassRoom, id=id)
        students = room.student.all().order_by('name')
        context ={
            'room':room,
            's' :students
        }
        return render (request,'class/classfiles.html',context)