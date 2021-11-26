from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.views import View
from django.contrib import messages
from classroom.models import ClassRoom, MemberShip
from profiles.models import Teacher, Student
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
# importing custom decorators
from src.decorators import SingleClassForbidden
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.conf import settings


#create classroom
class CreateClassRoom(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def get(self,request):
        return render(request,'class/create_class.html')
    
    def post(self,request):
        name = request.POST.get('name')
        unit = request.POST.get('unit')
        detail = request.POST.get('detail')
        user = request.user.teachers
        room = ClassRoom(teacher =user,unit=unit, name=name, details = detail )
        room.save()
        messages.success(request,'Classroom has been created')
        return redirect('teacher')

# view All class room
class ViewClassRoom(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self,reqeust):
        user = reqeust.user.teachers
        room = user.room.all()
        context = {
            'room':room
        }   
        return render(reqeust,'class/all_class.html',context)

# single class
@method_decorator(SingleClassForbidden,name='dispatch')
class SingleClass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request,id):
        
        room = get_object_or_404(ClassRoom  ,id=id) 
        stream = room.roomstream_set.all().order_by('-created_at')
        context ={
            'room':room,
            'stream':stream,
            'user':request.user
        } 
        return render(request,'class/single.html', context)

# Join Class
class JoinRoom(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)
    
    def post(self,request):
        code = request.POST.get('code')
        try :
            check_code = ClassRoom.objects.get(code = code)
            user = request.user.students
            class_room = ClassRoom(id = check_code.id )
            check = MemberShip.objects.filter(room=class_room, student = user )
            if check :
                messages.success(request,'You are already a member')
                return redirect('single', id=check_code.id) 
            else:
                member = MemberShip(room= class_room, student = user )
                member.is_join = True 
                member.save()
                messages.success(request,'Welcome to the Class')
                return redirect('single', id=check_code.id )  
        except ClassRoom.DoesNotExist:
            messages.warning(request,'Sorry the code did not Match. Try Again')
            return redirect('student')

# leave Class
class LeaveClass(View):
    @method_decorator(login_required(login_url='login'))
    def dispatch(self,request,*args,**kwargs):
        return super().dispatch(request,*args,**kwargs)

    def get(self, request,id):
        user = request.user.students
        room = get_object_or_404(ClassRoom, id=id)
        membership = MemberShip.objects.filter(student=user,room=room)
        membership.delete()
        messages.warning(request,'You have left the Classroom')
        return redirect('student')
