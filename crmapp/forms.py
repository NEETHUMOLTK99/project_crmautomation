from django.forms import ModelForm
from django import forms
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
import datetime


class CourseCreateForm(ModelForm):
    class Meta:
        model = Course
        fields = "__all__"
        widgets = {
            'course_name': forms.TextInput(attrs={'class': 'form-control'}),
            'course_duration': forms.TextInput(attrs={'class': 'form-control'}),
        }


class BatchCreateForm(ModelForm):
    class Meta:
        model = Batch
        fields = ['batch_code', 'course_name', 'start_date', 'fees', 'status']
        widgets = {
            'batch_code': forms.TextInput(attrs={'class': 'form-control'}),
            'course_name': forms.Select(attrs={'class': 'form-control'}),
            'Start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fees': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }

    def clean(self):
        cleaned_data = super().clean()
        # fees = cleaned_data.get('fees')
        #
        # if fees < 10000:
        #     msg = " Fees should be greater than 10000"
        #     self.add_error("fees", msg)



class CounsellorRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2',]
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
            'password2': forms.TextInput(attrs={'class': 'form-control'}),

        }

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class EnquiryCreateForm(ModelForm):
    class Meta:
        model = Enquiry
        fields = "__all__"
        widgets = {
            'enquiry_id': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'student_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'qualification': forms.TextInput(attrs={'class': 'form-control'}),
            'college': forms.TextInput(attrs={'class': 'form-control'}),
            'course': forms.Select(attrs={'class': 'form-control'}),
            'batch': forms.Select(attrs={'class': 'form-control'}),
            'followup_date': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),

        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['batch'].queryset = Batch.objects.none()

        if 'course' in self.data:
            try:
                course_id = int(self.data.get('course'))
                self.fields['batch'].queryset = Batch.objects.filter(course_name=course_id).order_by('enquiry')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['batch'].queryset = self.instance.course.batch_set.order_by('enquiry')

    def clean(self):
        cleaned_data = super().clean()
        followup_date = cleaned_data.get('followup_date')

        if followup_date < datetime.date.today():
            msg = " Follow Up date should be future date"
            self.add_error("followup_date", msg)


class AdmissionCreateForm(ModelForm):
    class Meta:
        model = Admissions
        fields = "__all__"
        widgets = {
            'admission_number': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'eid': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'fees': forms.TextInput(attrs={'class': 'form-control'}),
            'batch_code': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'}),

        }

    def clean(self):
        cleaned_data = super().clean()
        fees = cleaned_data.get('fees')

        if fees < 10000:
            msg = " Fees should be grater than 10000"
            self.add_error("fees", msg)

class StudentRegistraionForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'password1': forms.TextInput(attrs={'class': 'form-control'}),
        }

class PaymentCreateForm(ModelForm):
    class Meta:
        model = Payment
        fields = "__all__"
        widgets = {
            'admission_number': forms.TextInput(attrs={'class': 'form-control shadow-none bg-light', 'readonly': 'readonly'}),
            'amount': forms.TextInput(attrs={'class': 'form-control shadow-none bg-light'}),
            'date': forms.TextInput(attrs={'class': 'form-control', 'readonly shadow-none bg-light': 'readonly'}),
            'eid': forms.TextInput(attrs={'class': 'form-control', 'readonly shadow-none bg-light': 'readonly'}),

        }