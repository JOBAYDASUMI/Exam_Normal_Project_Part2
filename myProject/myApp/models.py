from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    USER = [
        ('recruiter','Recruiter'),
        ('jobseeker','Jobseeker'),
    ]
    user_type=models.CharField(choices=USER,max_length=100,null=True)
    profile_pic=models.ImageField(upload_to="Media/prifile_pic",null=True)
    
    def __str__(self):
        return f"{self.username}"
    
class JobModel(models.Model):
    JOB_TYPE_CHOICES=[
        ('full_time','Full_time'),
        ('part_time','Part_time'),
        ('contact','Contact'),
        ('internship','Internship'),
        ('temporary','Temporary'),
    ]
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE,blank=True)
    
    job_title=models.CharField(max_length=100,null=True,blank=True)
    company_name=models.CharField(max_length=100,null=True,blank=True)
    location=models.CharField(max_length=100,null=True,blank=True)
    description=models.TextField(null=True,blank=True)
    salary=models.PositiveIntegerField(null=True,blank=True)
    employee_type=models.CharField(max_length=100,null=True,blank=True,choices=JOB_TYPE_CHOICES)
    posted_date=models.DateTimeField(auto_now_add=True)
    application_dateline=models.DateTimeField(null=True,blank=True)
    
    def __str__(self):
        return f"{self.job_title}-{self.company_name}"
    
class jobApplyModel(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    job=models.ForeignKey(JobModel,on_delete=models.CASCADE,null=True)
    Resume=models.FileField(upload_to="Media/Resume",max_length=200,null=True,blank=True)
    Cover_letter=models.TextField(null=True,blank=True)
    Full_name=models.CharField(max_length=100,null=True,blank=True)
    Work_experience=models.CharField(max_length=100,null=True,blank=True)
    Skill=models.CharField(max_length=100,null=True,blank=True)
    Linkedin_URL=models.URLField(max_length=100,null=True,blank=True)
    Expected_salary=models.PositiveIntegerField(null=True,blank=True)
    
    
    
class jobApplyModel(models.Model):
    user=models.ForeignKey(CustomUser,null=True,on_delete=models.CASCADE)
    job=models.ForeignKey(JobModel,on_delete=models.CASCADE,null=True)
    Resume=models.FileField(upload_to="Media/Resume",max_length=200,null=True,blank=True)
    Cover_letter=models.TextField(null=True,blank=True)
    Full_name=models.CharField(max_length=100,null=True,blank=True)
    Work_experience=models.CharField(max_length=100,null=True,blank=True)
    Skill=models.CharField(max_length=100,null=True,blank=True)
    Linkedin_URL=models.URLField(max_length=100,null=True,blank=True)
    Expected_salary=models.PositiveIntegerField(null=True,blank=True)
