from django.views.generic import TemplateView, ListView
from jobs.models import Job
# Create your views here.
class HomePageView(ListView):
    model = Job
    context_object_name = 'job_list'
    template_name = 'home.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'