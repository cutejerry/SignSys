from django.contrib import admin
from SignModel.models import Course
from SignModel.models import Record

import csv
import codecs
from django.http import HttpResponse

class CourseAdmin(admin.ModelAdmin):
    pass

class RecordAdmin(admin.ModelAdmin):
    list_display = ('name','phone_num','created_time')
    search_fields = ('name','phone_num','course_list__name',)
    actions = ["export_as_csv"]
    list_per_page = 500

    def export_as_csv(self, request, queryset):
        opts = self.model._meta
        field_names = [f.name for f in opts.get_fields()]

        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment;filename={}.csv'.format(opts.verbose_name.encode('utf-8'))
        response.write(codecs.BOM_UTF8)
        writer = csv.writer(response)
        writer.writerow(field_names)

        for obj in queryset:
            row = []
            for field in field_names:
                if(field == 'course_list'):
                    info = ""
                    for s in getattr(obj, "course_list").all():
                        info = info + s.name + ','
                    info = info[:-1]
                else:
                    info = getattr(obj, field)
                row.append(info)
            writer.writerow(row)

        return response
    export_as_csv.short_description = "导出成csv"

# Register your models here.
admin.site.register(Course, CourseAdmin)
admin.site.register(Record, RecordAdmin)