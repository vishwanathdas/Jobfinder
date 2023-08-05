# backend/recruitment_app/views.py
from django.shortcuts import render, redirect,HttpResponseRedirect
from .models import Job, Candidate
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import Group
from django.contrib import messages

@login_required
@permission_required('app.recruiter', raise_exception=True)
def job_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        description = request.POST['description']
        job_type = request.POST['job_type']
        location = request.POST['location']
        posted_by = request.user
        Job.objects.create(title=title, description=description, job_type=job_type, location=location, posted_by=posted_by)
        messages.success(request,'Your Job successfully Post !!')
        return redirect('home')

    return render(request, 'app/job_post.html')

def apply_job(request, job_id):
    job = Job.objects.get(pk=job_id)
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        resume = request.FILES['resume']
        Candidate.objects.create(name=name, email=email, resume=resume)
        messages.success(request,'Your Job successfully apply !!')
        return redirect('home')

    return render(request, 'app/apply_job.html', {'job': job})

def home(request):
    stu=Job.objects.all()
    return render(request,"app/home.html",{'stu':stu})


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,'Your Account has been create successfully  !!')
            user_group = request.POST.get('user_group')
            if user_group == 'recruiter':
                group = Group.objects.get(name='Recruiters')
            else:
                group = Group.objects.get(name='Candidates')
            user.groups.add(group)
            return HttpResponseRedirect('/login/')
    else:
        form = UserCreationForm()

    return render(request, 'app/register.html', {'form': form})


def user_login(request):
  if not request.user.is_authenticated:
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request,'Your Account successfully Login !!')
            return redirect('/')  # Assuming you have a 'home' URL pattern

    else:
        form = AuthenticationForm()

    return render(request, 'app/login.html', {'form': form})
  else:
     return HttpResponseRedirect('/')

def user_logout(request):
    logout(request)
    messages.success(request,'Your Account successfully Logout !!')
    return redirect('login')  # Redirect to the login page after logout