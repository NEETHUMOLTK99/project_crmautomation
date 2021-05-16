"""crmautomation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *
from django.shortcuts import render

urlpatterns = [
    path("",lambda request:render(request,"crmapp/ch_base.html")),

    path('course',Course_Registration.as_view(),name='course'),
    path('course_edit/<int:id>',Course_edit.as_view(),name="course_edit"),
    path('course_delete/<int:id>',Course_delete.as_view(),name="course_delete"),
    path('batch', Batch_Creation.as_view(), name='batch'),
    path('batch_edit/<int:id>', Batch_edit.as_view(), name='batch_edit'),
    path('batch_delete/<int:id>', Batch_delete.as_view(), name='batch_delete'),
    path('cs_register', CounsellorRegistration.as_view(), name='cs_register'),
    path('cs_login', CounsellorLogin.as_view(), name='cs_login'),

    path('cs_view', Counsellor_View.as_view(), name='cs_view'),
    path('cs_edit/<int:id>', Counsellor_Edit.as_view(), name='cs_edit'),
    path('cs_delete/<int:id>', Counsellor_Delete.as_view(), name='cs_delete'),
    path('enquiry', Enquiry_Creation.as_view(), name='enquiry'),
    path('enquiry_edit/<int:id>', Enquiry_Edit.as_view(), name='enquiry_edit'),
    path('enquiry_delete/<int:id>', Enquiry_Delete.as_view(), name='enquiry_delete'),
    path('followup', Follow_up.as_view(), name='followup'),
    path('admission/<int:id>', Admission_Creation.as_view(), name='admission'),
    path('admission_edit/<int:id>', Admission_Edit.as_view(), name='admission_edit'),
    path('admission_delete/<int:id>', Admission_Delete.as_view(), name='admission_delete'),
    path('st_view<int:id>', Student_Details.as_view(), name='st_view'),
    path('st_register<int:id>', Student_Registration.as_view(), name='st_register'),
    path('st_login', Student_login.as_view(), name='st_login'),
    path('pay', Student_Payments.as_view(), name='pay'),
    path('home', DashBoard.as_view(), name='home'),
    path('ajax/load-course/', load_course, name='ajax_load_course'),

]

