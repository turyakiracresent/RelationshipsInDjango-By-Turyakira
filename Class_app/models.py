from django.db import models

class Department(models.Model):
    department_id = models.CharField(primary_key=True, max_length=100)
    department_name = models.CharField(max_length=100)
    head_of_department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.department_id} {self.department_name} ({self.department_name})"


class Staff (models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Staff_id = models.IntegerField(primary_key=True,unique=True)
    Department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)  

    def __str__(self):
        return f"{self.First_name} {self.Last_name} {self.Department} ({self.Staff_id})"

class Student (models.Model):
    First_name = models.CharField(max_length=100)
    Last_name = models.CharField(max_length=100)
    Student_id = models.IntegerField(primary_key=True, unique=True)
    # Staff_id = models.IntegerField()
    
    def __str__(self):
        return f"{self.First_name} {self.Last_name} ({self.Student_id})"
    

class Address_Student(models.Model):
    # student = models.OneToOneField(Student, on_delete=models.CASCADE)
    student = models.OneToOneField(Student, on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    subcounty = models.CharField(max_length=255)
    village = models.CharField(primary_key=True,max_length=255)

    def __str__(self):
        return f"{self.student} {self.subcounty} ({self.village})"

class Address_Staff(models.Model):
    # staff = models.OneToOneField(Staff, on_delete=models.CASCADE)
    staff = models.OneToOneField(Staff, on_delete=models.SET_NULL, null=True)
    country = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    subcounty = models.CharField(max_length=255) 
    village = models.CharField(primary_key=True,max_length=255)

    def __str__(self):
        return f"{self.staff} {self.subcounty} ({self.village})"
    

    
class Course(models.Model):
    course_id = models.CharField(primary_key=True, max_length=100)
    course_name = models.CharField(max_length=100)
    course_code = models.CharField(max_length=10, unique=True)
    credits = models.IntegerField()
    department = models.ManyToManyField(Department)

    def __str__(self):
        return f"{self.course_name} ({self.course_code})"
    
    