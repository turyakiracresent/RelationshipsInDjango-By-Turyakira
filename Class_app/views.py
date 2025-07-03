from django.views.generic import ListView
from .models import Staff, Student , Address_Student , Address_Staff, Department, Course

# view for staff
class StaffList(ListView):
    model = Staff
    template_name = "staff.html"


#view for the students
class StudentList(ListView):
    model = Student
    template_name = "student.html"

class AddressStudentList(ListView):
    model = Address_Student
    template_name = "address_student.html"

class AddressStaffList(ListView):
    model = Address_Staff
    template_name = "address_staff.html"

class DepartmentList(ListView):
    model = Department
    template_name = "department.html"   

class CourseList(ListView):
    model = Course
    template_name = "course.html"



