from django.contrib import admin
from .models import Staff,Student,Address_Student,Address_Staff,Department,Course 
# Register your models here.
admin.site.register(Staff)

admin.site.register(Student)

admin.site.register(Address_Student)

admin.site.register(Address_Staff)

admin.site.register(Department)

admin.site.register(Course)


