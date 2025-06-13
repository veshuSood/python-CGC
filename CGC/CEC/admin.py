from django.contrib import admin
from .models import Student
# Register your models here.
# admin.site.register(Student)
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'roll_number', 'email')
    search_fields = ('name', 'roll_number')