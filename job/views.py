from django.shortcuts import redirect, render
from django.urls import reverse
from .models import job, Apply
from django.core.paginator import Paginator
from .forms import applyfrom,jobform
from django.contrib.auth.decorators import login_required
from .filters import JobFilter


# Create your views here.


def job_list(request):
    job_list=job.objects.all()
    myfilter = JobFilter(request.GET, queryset=job_list)
    job_list=myfilter.qs

    paginator = Paginator(job_list, 3)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context={'jobs':page_obj,'myfilter':myfilter}
    print(myfilter.form)  # Debugging statement
    return render(request,'job/jobs.html',context)


def job_details(request,slug):
    job_details=job.objects.get(slug=slug)
    if request.method=='POST':
        form=applyfrom(request.POST , request.FILES)
        print('test')
        if form.is_valid():
            myform=form.save(commit=False)
            myform.job=job_details
            myform.save()
            print('Done')


    
    else:
        form=applyfrom()
    
    context={'job':job_details,'form1':form}
    return render(request,'job/job_details.html',context)


@login_required
def add_job(request):

        if request.method=='POST':
            form=jobform(request.POST, request.FILES)
            if form.is_valid():
                myform=form.save(commit=False)
                myform.owner=request.user
                myform.save()
                return redirect(reverse('jobs:job_list'))


        else:
            form=jobform()

        return render(request,'job/add_job.html',context={'form':form})
