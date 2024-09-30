from django.shortcuts import render,redirect,get_object_or_404
from myApp.models import *
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required






def homePage(req):

    return render(req,'common/homePage.html')

def logoutPage(req):
    logout(req)
    return redirect("loginPage")

def loginPage(req):
    if req.method == 'POST':
        Username=req.POST.get('username')
        Password=req.POST.get('password')
        user = authenticate(username=Username,password=Password)
        
        if user:
            login(req,user)
            return redirect("jobFeedPage")
        else:
            messages.warning(req,'User Not Found')

    return render(req,'common/loginPage.html')

def registerPage(req):
    if req.method == 'POST':
        Username=req.POST.get('username')
        Usertype=req.POST.get('usertype')
        Email=req.POST.get('email')
        Password=req.POST.get('password')
        Confirmpassword=req.POST.get('confirmpassword')
        
        if Password == Confirmpassword:
            user = CustomUser.objects.create_user(
                username=Username,
                user_type=Usertype,
                email=Email,
                password=Confirmpassword,
                
            )
        messages.success(req,"Account Create Success fully")
        return redirect("loginPage")
            
            

    return render(req,'common/registerPage.html')
@login_required
def jobFeedPage(req):
    
    Job=JobModel.objects.all()
    
    context={
        'Job':Job
    }

    return render(req,'includes/jobFeedPage.html',context)

def addJobPage(req):
    
    current_user = req.user
    if current_user.user_type == 'recruiter':
        
        if req.method== 'POST':
            job=JobModel()
            job.job_title=req.POST.get('job_title')
            job.company_name=req.POST.get('company_name')
            job.location=req.POST.get('location')
            job.description=req.POST.get('description')
            job.salary=req.POST.get('salary')
            job.employee_type=req.POST.get('employee_type')
            job.application_dateline=req.POST.get('application_deadline')
            job.save()
            messages.success(req,"Job Create Successfully")
            return redirect('jobFeedPage')
        
        return render (req,'myAdmin/addJobPage.html')
    else:
        messages.warning(req,"You Are Not Recruter")
        
        
def applyNow(req,apply_id):
    
    current_user=req.user
    
    if current_user.user_type == 'jobseeker':
        specific_job=JobModel.objects.get(id=apply_id)
        already_exists=jobApplyModel.objects.filter(user=current_user,job=specific_job).exists()
        
        context={
            'specific_job': specific_job,
            'already_exists': already_exists
            
        }
        if req.method == 'POST':
            Full_name=req.POST.get('full_name')
            Work_experience=req.POST.get('work_experience')
            Skill=req.POST.get('skill')
            Linkedin_url=req.POST.get('linkedin_url')
            Expected_salary=req.POST.get('expected_salary')
            Resume=req.POST.get('resume')
            Cover_letter=req.POST.get('cover_letter')
            
            apply=jobApplyModel(
                Full_name=Full_name,
                Work_experience=Work_experience,
                Skill=Skill,
                Linkedin_URL=Linkedin_url,
                Expected_salary=Expected_salary,
                Resume=Resume,
                Cover_letter=Cover_letter,
            )
            apply.save()
            return redirect("jobFeedPage")
            
            
        
        return render(req,'myAdmin/applyNow.html',context)
    
    else:
        messages.warning(req,"You Are Not JobSeeker")
        
        
def profilePage(req):
    
    return render(req,'common/profilePage.html')
        
    
    
def createJob(req):
    current_user=req.user
    job=JobModel.objects.filter(user=current_user)

    context ={
        'job':job
    }

    return render(req,"myAdmin/createJob.html",context)  

def editJob(req,id):

    job=JobModel.objects.get(id=id)

    current_user=req.user
    if current_user.user_type == 'recruiter':
        if req.method=='POST':
            job=JobModel()
            job.id=req.POST.get('job_id')
            job.user=current_user
            job.job_title=req.POST.get('job_title')
            job.company_name=req.POST.get('company_name')
            job.location=req.POST.get('location')
            job.description=req.POST.get('description')
            job.salary=req.POST.get('salary')
            job.employee_type=req.POST.get('employee_type')
            job.application_dateline=req.POST.get('application_deadline')

    context={
        'job': job
    }

    return render(req,"myAdmin/editJob.html",context)

def deletejob(req,id):
    job=JobModel.objects.get(id=id).delete()

    return redirect("createJob")