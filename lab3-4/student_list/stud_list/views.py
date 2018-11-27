from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Student

# Create your views here.
def myView(request):
	all_students = Student.objects.all().order_by('-mark',)


	return render(request,'list.html',
		 {'all_students': all_students})
def addStudent(request):
	z = request.POST["name"]
	x = request.POST["mark"]
	new_student = Student(name = z, mark = x)
	new_student.save()
	return HttpResponseRedirect('/list/')

def deleteStudent(request,student_id):
	student_to_delete = Student.objects.get(id = student_id)
	student_to_delete.delete()
	return HttpResponseRedirect('/list/')
def changeStudent(request,student_id):
	z = request.POST["name"]
	x = request.POST["mark"]
	student_to_change = Student.objects.get(id = student_id)
	student_to_change.name = z
	student_to_change.mark = x
	student_to_change.save()

	return HttpResponseRedirect('/list/')



