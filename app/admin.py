from django.contrib import admin
from .models import Job,Candidate
# Register your models here.
 
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display=['id','title','description','job_type','location','posted_by']


@admin.register(Candidate)
class CondidateAdmin(admin.ModelAdmin):
    list_display=['id','email','name','resume']    