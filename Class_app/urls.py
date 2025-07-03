from django.urls import path
from .views import StaffList, StudentList, AddressStudentList, AddressStaffList, DepartmentList, CourseList
# URL configuration for Class_app
urlpatterns = [
    path('', StaffList.as_view(), name='staff'),
    path('student/', StudentList.as_view(), name='student'),
    path('address_student/', AddressStudentList.as_view(), name='address_student'),
    path('address_staff/', AddressStaffList.as_view(), name='address_staff'),   
    path('department/', DepartmentList.as_view(), name='department'),
    path('course/', CourseList.as_view(), name='course'),
  

]
