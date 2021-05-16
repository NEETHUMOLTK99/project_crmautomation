from django.db import models
from datetime import date
# Create your models here.

class Course(models.Model):
    course_name = models.CharField(max_length=20, unique=True)
    course_duration = models.CharField(max_length=20)

    def __str__(self):
        return self.course_name

class Batch(models.Model):
    batch_code = models.CharField(max_length=20, unique=True)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField()
    fees = models.IntegerField()
    choices = (('yet to begin', 'yet to begin'), ('in progress', 'in progress'), ('completed', 'completed'))
    status = models.CharField(max_length=20, choices=choices)

    def __str__(self):
        return self.batch_code

class Enquiry(models.Model):
    enquiry_id = models.CharField(max_length=20, unique=True)
    student_name = models.CharField(max_length=20)
    address = models.TextField()
    email = models.EmailField(max_length=50)
    phone = models.IntegerField(max_length=20)
    qualification = models.CharField(max_length=50)
    college = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch = models.ForeignKey(Batch, on_delete=models.CASCADE)
    followup_date = models.DateField()
    choices = (('admited', 'admited'), ('not admited','not admited'))
    status = models.CharField(max_length=20, choices=choices)
    def __str__(self):
        return str(self.enquiry_id) + str(self.course)

class Admissions(models.Model):
    admission_number = models.CharField(max_length=20, unique=True)
    eid = models.CharField(max_length=20, unique=True)
    fees = models.IntegerField()
    batch_code = models.CharField(max_length=20)
    date = models.DateField(default=date.today())
    def __str__(self):
        return str(self.admission_number)
class Payment(models.Model):
    admission_number = models.CharField(max_length=20, unique=True)
    amount = models.IntegerField()
    date = models.DateField(default=date.today())
    eid = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.admission_number
