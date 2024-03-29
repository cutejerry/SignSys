from django.shortcuts import render
from SignModel.models import Course
from SignModel.models import Record
from django.http import HttpResponse

# Create your views here.
def sign(request):
    course_list = list(Course.objects.all().order_by('name'))
    return render(request, 'sign.html', {'course_list': course_list})


def signfinish(request):
    #storage in database
    if request.method == 'POST':
        name = request.POST.get("name")
        grade = request.POST.get("grade_list")
        courses = request.POST.getlist("courses")
        phone_num = request.POST.get("phone_num")
        email = request.POST.get("email")
        (object, created) = Record.objects.get_or_create(phone_num=phone_num)
        if created != True:
            print("The record is created. We update it now.")
        object.name=name
        object.grade=grade
        object.email=email
        for c in courses:
            obj = Course.objects.get(name=c)
            object.course_list.add(obj)
        object.save()
        return render(request, 'signfinish.html')
    else:
        return render(request, 'signfinish.html') #for weichat flow