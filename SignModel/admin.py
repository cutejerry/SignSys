from django.contrib import admin
from SignModel.models import Course
from SignModel.models import Record

class CourseAdmin(admin.ModelAdmin):
    pass

class RecordAdmin(admin.ModelAdmin):
    list_display = ('name','phone_num','created_time')
    search_fields = ('name','phone_num','course_list__name',)

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Record, RecordAdmin)