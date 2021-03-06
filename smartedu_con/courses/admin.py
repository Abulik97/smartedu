from django.contrib import admin
from.models import Course,Category,Tag
# Register your models here.
@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('name','available')
    list_filter=('available',)
    search_fields=('name','description')

@admin.register(Category)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}  



@admin.register(Tag)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}      