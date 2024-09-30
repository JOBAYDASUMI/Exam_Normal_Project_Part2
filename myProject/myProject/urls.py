
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from myProject.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homePage/',homePage,name='homePage'),
    path('',loginPage,name='loginPage'),
    path('logoutPage/',logoutPage,name='logoutPage'),
    path('registerPage/',registerPage,name='registerPage'),
    path('jobFeedPage/',jobFeedPage,name='jobFeedPage'),
    path('addJobPage/',addJobPage,name='addJobPage'),
    path('applyNow/<str:apply_id>',applyNow, name='applyNow'),
    
    path('profilePage/',profilePage,name='profilePage'),
    path('createJob/',createJob,name='createJob'),

    path('editJob/<str:id>',editJob, name='editJob'),
    path('deletejob/<str:id>',deletejob, name='deletejob'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
