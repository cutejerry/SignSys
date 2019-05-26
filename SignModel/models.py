from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=128, unique=True, verbose_name="已有课程")

    def __str__(self):
        return self.name

# Create your models here.
class Record(models.Model):
    name = models.CharField(max_length=64, verbose_name="已登记记录")
    grade = models.CharField(max_length = 1, default = "0")
    course_list = models.ManyToManyField("Course")
    phone_num = models.CharField(max_length=13, unique=True, verbose_name="电话号码")
    email = models.EmailField(null = True, blank = True)
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    def __str__(self):
        return self.name