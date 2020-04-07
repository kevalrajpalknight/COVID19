from django.views.generic import TemplateView, ListView
from Aware.models import Case,Location
from django.db.models import Count
import json
def join(Case,Location):
    location = []
    for case in Case.objects.all():
        location.append({"lng":case.address.longitude,"lat":case.address.latitude})
    return location

class Home(ListView):
    template_name = 'index.html'
    model = Case
    def queryset(self): return {"Cases":Case.objects.all().values('address', 'case_type','user').annotate(total=Count('address')).order_by('address','total','case_type'),
                "Location": join(Case, Location)}

class TestPage(TemplateView):
	template_name = 'test.html'
class ThanksPage(TemplateView):
	template_name = 'thanks.html'