from django.contrib import admin
from myApp.models import *

class CustomUser_Display(admin.ModelAdmin):
    list_display=['username','user_type','email']

admin.site.register(CustomUser,CustomUser_Display)

class JobModel_Display(admin.ModelAdmin):
    list_display=['job_title','company_name','location','salary']
    
admin.site.register(JobModel,JobModel_Display)


class jobApplyModel_Display(admin.ModelAdmin):
    list_display=['user','job','Full_name','Work_experience','Skill','Expected_salary']
    
admin.site.register(jobApplyModel,jobApplyModel_Display)
