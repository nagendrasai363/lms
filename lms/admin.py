from django.contrib import admin

# Register your models here.
from lms.models import Course,Module,Lesson,CourseStatus,Category

import nested_admin


class LessonInline(nested_admin.NestedStackedInline):
    model = Lesson

class ModuleInline(nested_admin.NestedStackedInline):
    model = Module
    inlines = [LessonInline]

class CourseAdmin(nested_admin.NestedModelAdmin):
    inlines = [ModuleInline]

admin.site.register(CourseStatus)

admin.site.register(Course, CourseAdmin)

admin.site.register(Category)