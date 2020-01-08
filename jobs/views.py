from django.views.generic import ListView, DetailView

from .models import Job
# Create your views here.
 
#class JobListView(ListView):
#    model = Job
#    context_object_name = 'job_list'
#    template_name = 'home.html'

class JobDetailView(DetailView):
    model = Job
    context_object_name = 'job'
    template_name = 'jobs/job_detail.html'