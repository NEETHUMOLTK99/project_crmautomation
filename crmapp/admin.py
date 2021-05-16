
# Register your models here.
from django.contrib import admin
from .models import Payment,Enquiry,Admissions
admin.site.register(Payment),
admin.site.register(Enquiry),
admin.site.register(Admissions)