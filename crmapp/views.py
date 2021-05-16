from django.shortcuts import render,redirect
from .models import Course,Batch,Enquiry,Admissions,Payment
from .forms import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from django.views.generic import TemplateView
from django.core.paginator import Paginator
from datetime import date


# Create your views here.
class Course_Registration(TemplateView):
    model=Course
    form_class=CourseCreateForm
    template_name='crmapp/ch_course_reg.html'
    def get(self,request,*args,**kwargs):
        courses =Course.objects.all()
        self.context={
            "form":self.form_class,
            "courses":courses
        }

        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            courses = Course.objects.all()
            self.context = {
                "form": self.form_class,
                "courses": courses
            }
            return render(request, self.template_name, self.context)
        else:
            self.context = {
                "form": self.form_class
            }
            return render(request, self.template_name, self.context)
class Course_edit(TemplateView):
    model = Course
    form_class = CourseCreateForm
    template_name = 'crmapp/ch_course_reg.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        courses = self.get_object(id)
        form = self.form_class(instance=courses)
        self.context = {
            "form":form,

        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        courses = self.get_object(id)
        form = self.form_class(request.POST, instance=courses)
        if form.is_valid():
            form.save()
            return redirect('course')
        return render(request, self.template_name, self.context)

class Course_delete(TemplateView):
    model = Course
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        course = self.get_object(id)
        course.delete()
        return redirect('course')

class Batch_Creation(TemplateView):
    model = Batch
    form_class = BatchCreateForm
    template_name = 'crmapp/ch_batch_creation.html'

    def get(self, request, *args, **kwargs):
        batches = Batch.objects.all()[::-1]
        paginator = Paginator(batches, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        self.context = {
            "form": self.form_class,
            "page_obj": page_obj
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            batches = Batch.objects.all()
            self.context = {
                "form": self.form_class,
                "batches": batches
            }
            return render(request, self.template_name, self.context)
        else:
            self.context = {
                "form": self.form_class
            }
            return render(request, self.template_name, self.context)

class Batch_edit(TemplateView):
    model = Batch
    form_class = BatchCreateForm
    template_name = 'crmapp/ch_batch_creation.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        batches = self.get_object(id)
        form = self.form_class(instance=batches)
        self.context = {
            "form":form,

        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        batches = self.get_object(id)
        form = self.form_class(request.POST, instance=batches)
        if form.is_valid():
            form.save()
            return redirect('batch')
        # self.context = {
        #     "form": self.form_class
        # }

        return render(request, self.template_name, self.context)

class Batch_delete(TemplateView):
    model = Batch
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        batch = self.get_object(id)
        batch.delete()
        return redirect('batch')


class CounsellorRegistration(TemplateView):
    form_class = CounsellorRegistrationForm
    template_name = 'crmapp/ch_counsellor_reg.html'
    def get(self, request, *args, **kwargs):
        self.context = {
            "form":self.form_class
        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('cs_login')
        else:
            self.context = {
                "form":form
            }
            return render(request, self.template_name, self.context)
class CounsellorLogin(TemplateView):
    # form_class = LoginForm
    template_name = 'crmapp/cs_login.html'
    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)
    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            username = request.POST.get("uname")
            password = request.POST.get("pwd")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request,user)
                return redirect('enquiry')
            else:
              return render(request,'crmapp/login.html',{"message":"invalid password or username"})
        return render(request,'crmapp/login.html')



class Counsellor_View(TemplateView):
    model = User
    template_name = 'crmapp/ch_counsellors.html'
    def get(self, request, *args, **kwargs):
        counsellors = User.objects.all()
        self.context = {
            "counsellors":counsellors
        }
        return render(request, self.template_name, self.context)

class Counsellor_Edit(TemplateView):
    model = User
    form_class = CounsellorRegistrationForm
    template_name = 'crmapp/ch_counsellor_reg.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        counsellors = self.get_object(id)
        form = self.form_class(instance=counsellors)
        self.context = {
            "form":form,

        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        counsellors = self.get_object(id)
        form = self.form_class(request.POST, instance=counsellors)
        if form.is_valid():
            form.save()
            return redirect('cs_view')
        return render(request, self.template_name, self.context)

class Counsellor_Delete(TemplateView):
    model = User

    def get_object(self, id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        cs = self.get_object(id)
        cs.delete()
        return redirect('cs_view')

class Enquiry_Creation(TemplateView):
    model = Enquiry
    form_class = EnquiryCreateForm
    template_name = 'crmapp/cs_student_enquiry.html'
    def get(self, request, *args, **kwargs):

        enquiry = self.model.objects.last()
        if enquiry:
            last_eid = enquiry.enquiry_id
            lst = int(last_eid.split('-')[1]) + 1
            eid = 'EID-' + str(lst)
        else:
            eid = 'EID-1000'
        form = self.form_class(initial={'enquiry_id': eid})
        students = Enquiry.objects.all()[::-1]
        paginator = Paginator(students, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        self.context = {
            "form":form,
            "page_obj": page_obj
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            students = Enquiry.objects.all()
            self.context = {

                "students": students
            }
            return redirect('enquiry')
        else:
            self.context = {
                "form": self.form_class
            }
            return render(request, self.template_name, self.context)

def load_course(request):
    course_id = request.GET.get('course_id')
    batches = Batch.objects.filter(course_name=course_id).all()
    return render(request, 'crmapp/course_dropdown.html', {'batches': batches})
    # return JsonResponse(list(cities.values('id', 'name')), safe=False)

class Enquiry_Edit(TemplateView):
    model = Enquiry
    form_class = EnquiryCreateForm
    template_name = 'crmapp/cs_student_enquiry.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        students = self.get_object(id)
        form = self.form_class(instance=students)
        self.context = {
            "form":form,
        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        students = self.get_object(id)
        form = self.form_class(request.POST, instance=students)
        self.context = {
            "form": form
        }
        if form.is_valid():
            #eid = form.cleaned_data.get("enquiry_id")

            form.save()
            return redirect('enquiry')
        return render(request, self.template_name, self.context)

class Enquiry_Delete(TemplateView):
    model = Enquiry

    def get_object(self, id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        student = self.get_object(id)
        student.delete()
        return redirect('enquiry')


class Follow_up(TemplateView):
    model = Enquiry
    template_name = "crmapp/cs_followup_date.html"
    def get(self, request, *args, **kwargs):
        dates = Enquiry.objects.filter(followup_date=date.today())
        self.context = {
            "dates":dates
        }
        return render(request, self.template_name, self.context)

class Admission_Creation(TemplateView):
    model = Admissions
    form_class = AdmissionCreateForm
    template_name = 'crmapp/cs_admissions.html'

    def get_object(self, id):
        return Enquiry.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        admission = self.model.objects.last()
        id = kwargs.get("id")
        students = self.get_object(id)

        if admission:
            last_adm = admission.admission_number
            lst = int(last_adm.split('-')[1]) + 1
            adm = 'LMNR-' + str(lst)
        else:
            adm = 'LMNR-1000'
        admissions = Admissions.objects.all()
        eid = students.enquiry_id
        batch = students.batch
        form = self.form_class(initial={'admission_number': adm, 'eid': eid, 'batch_code': batch})
        #eid = students.enquiry_id
        #batch = students.batch
        #batchcode = Enquiry.objects.filter(batch__batch_code=batch)
        #bcode = [b.batch for b in batchcode]
        #for i in bcode:
         #   code = i.batch_code

        #form = self.form_class(initial={'admission_number': adm,'eid':eid, 'batch_code':code})

        paginator = Paginator(admissions, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        self.context = {
            "form": form,
            "page_obj": page_obj
        }

        return render(request, self.template_name, self.context)

    # def post(self, request, *args, **kwargs):
    #     form = self.form_class(request.POST)
    #
    #     if form.is_valid():
    #         form.save()
    #         admissions = Admissions.objects.all()
    #         self.context = {
    #             "form":form,
    #             "admissions": admissions
    #         }
    #         return render(request, self.template_name, self.context)
    #     else:
    #         return HttpResponse("error")
            # self.context = {
            #     "form": self.form_class
            # }
            # return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            admissions = Admissions.objects.all()
            self.context = {

                "admissions": admissions
            }
            return render(request, self.template_name, self.context)
        else:
            self.context = {
                "form": form
            }
            return render(request, self.template_name, self.context)


class Admission_Edit(TemplateView):
    model = Admissions
    form_class = AdmissionCreateForm
    template_name = 'crmapp/cs_admissions.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        admissions = self.get_object(id)
        form = self.form_class(instance=admissions)
        self.context = {
            "form":form,
        }
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("id")
        admissions = self.get_object(id)
        form = self.form_class(request.POST, instance=admissions)
        if form.is_valid():
            form.save()
            admissions = Admissions.objects.all()[::-1]
            paginator=Paginator(admissions,3)
            page_number=request.GET.get('page')
            page_obj=paginator.get_page(page_number)


            self.context = {
                "form": self.form_class,
                "page_obj":page_obj
            }
            return render(request, self.template_name, self.context)

        return render(request, self.template_name, self.context)

class Admission_Delete(TemplateView):
    model = Admissions
    form_class = AdmissionCreateForm
    template_name = 'crmapp/cs_admissions.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)

    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        admission = self.get_object(id)
        admission.delete()
        admissions = Admissions.objects.all()
        self.context = {
            "form": self.form_class,
            "admissions": admissions
        }
        return render(request, self.template_name, self.context)


class Student_Details(TemplateView):
    model = Admissions
    template_name = 'crmapp/cs_student_details.html'
    def get_object(self, id):
        return self.model.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        admissions = self.get_object(id)
        eid = admissions.eid

        students = Enquiry.objects.get(enquiry_id=eid)
        self.context = {
            'admissions':admissions,
            'students':students
        }
        return render(request, self.template_name, self.context)

class Student_Registration(TemplateView):
    form_class = StudentRegistraionForm
    template_name = 'crmapp/ch_counsellor_reg.html'
    def get_object(self, id):
        return Admissions.objects.get(id=id)
    def get(self, request, *args, **kwargs):
        id = kwargs.get("id")
        admission = self.get_object(id)
        admission_number = admission.admission_number
        eid = admission.eid
        form = self.form_class(initial={'username': admission_number, 'password1': eid })
        self.context = {
            "form":form
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return redirect('st_login')
        else:
            self.context = {
                "form": form
            }
            return render(request, self.template_name, self.context)

class Student_login(TemplateView):
    # form_class = LoginForm
    template_name = 'crmapp/cs_login.html'

    def get(self, request, *args, **kwargs):

        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):

        if request.method == 'POST':
            username = request.POST.get("uname")
            password = request.POST.get("pwd")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('pay')
            else:
                return render(request, 'crmapp/login.html', {"message": "invalid usernam or password"})
        return render(request,'crmapp/login.html')

class Student_Payments(TemplateView):
    model = Payment
    form_class = PaymentCreateForm
    template_name = 'crmapp/st_payment.html'
    def get(self, request, *args, **kwargs):
        admission = Admissions.objects.get(admission_number=request.user)
        admission_number = admission.admission_number


        eid = admission.eid

        form = self.form_class(initial={'admission_number': admission_number, 'eid': eid})
        #payments = Payment.objects.get(admission_number=request.user)
        self.context = {
            "form": form,
            #"payments":payments
        }
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            #payments = Payment.objects.get(admission_number=request.user)
            self.context = {
                "form": self.form_class,
                #"payments": payments
            }
            return render(request, self.template_name, self.context)
        else:
            self.context = {
                "form": self.form_class
            }
            return render(request, self.template_name, self.context)





class DashBoard(TemplateView):
    template_name = 'crmapp/admin.html'
    def get(self, request, *args, **kwargs):
        context = {}
        lst = []
        status = 'yet to begin'
        dic = {}
        dic1 = {}
        batch = Batch.objects.filter(status=status)
        admision = Admissions.objects.filter(batch_code__in=[b.batch_code for b in batch])
        enquiry = Enquiry.objects.filter(enquiry_id__in=[a.eid for a in admision])
        course = [e.course for e in enquiry]

        for obj in course:
            if obj not in dic1:
                lst.append(str(obj))

                dic1[obj] = 1
            else:
                dic1[obj]+=1

        for key, value in dic1.items():

            if key not in dic:
                dic[str(key)] = value

        count = str(len(lst))



        #Pending Fees

        status = "in progress"
        f_batch = Batch.objects.filter(status=status)
        f_admision = Admissions.objects.filter(batch_code__in=[b.batch_code for b in f_batch])
        fees = [a.fees for a in f_admision]
        #print(fees)
        f_enquiry = Enquiry.objects.filter(enquiry_id__in=[a.eid for a in f_admision])
        crse = [e.course for e in f_enquiry]
        course_1 = {}
        course_2 = {}
        count_1 = []

        #total = f_admision["fees__sum"]
        #print(total)
        pay = Payment.objects.filter(admission_number__in=[a.admission_number for a in f_admision])
        amount = [p.amount for p in pay]
        fees = [a.fees for a in f_admision]
        total = [x1 - x2 for (x1, x2) in zip(fees, amount)]
        for obj in crse:
            if obj not in course_1:
                count_1.append(obj)
                course_1[obj] = None
            else:
                course_1[obj] = None

        for fee in total:
            course_1[obj] = fee

        for key, value in course_1.items():

            if key not in dic:
                course_2[str(key)] = value

        #print(course_2)
        count1= str(len(count_1))

        context = {
            "dic": dic,
            "lst": lst,
            "count": count,

            "course":course_2,
            "count_1": count1,

        }

        return render(request, self.template_name, context)
        return render(request, self.template_name, context)