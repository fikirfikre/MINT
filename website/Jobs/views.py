from django.shortcuts import render,get_object_or_404
from .models import Jobs
from .forms import JobPostForm
from django.core.mail import EmailMessage
from django.conf import settings

# Create your views here.


def jobs_list(request):
    jobs = Jobs.published.all()
    return render(request,'jobs/list.html',{'jobs':jobs})

def jobs_detail(request,id):
    job = get_object_or_404(Jobs,id=id,status = Jobs.Status.PUBLISHED)
    return render(request,'jobs/detail.html',{'job':job})


def apply_job(request,job_id):
    job = get_object_or_404(Jobs,id=job_id,status =Jobs.Status.PUBLISHED)
    sent=False
    job_cv = None
    if request.method == "POST" and request.FILES['file']:
        form =JobPostForm(request.POST,files = request.FILES)

        if form.is_valid():
         
            job_cv = form.save(commit = False)
            job_cv.job = job
            file_path = job_cv.file.path
            job_cv.save()
            
          
            subject = f"{job_cv.name} send cv for {job.title}"
            email = f"{job_cv.name }email: {job_cv.email}"
            email_message = EmailMessage(subject,email,job_cv.email,['fikirteshome15@gmail.com',job_cv.email])
            email_message.content_type ='pdf'
            uploaded_file = request.FILES['file']
            email_message.attach(uploaded_file.name,uploaded_file.read(),uploaded_file.content_type)
            email_message.send(),
          
          
            sent=True

    else:
            form = JobPostForm()

    return render(request,'jobs/apply.html',{'job':job,'form':form,'sent':sent})
