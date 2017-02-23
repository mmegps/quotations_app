from django.shortcuts import render
from quotations.models import Qs

# Create your views here.
def index(request):
	count = Qs.objects.count()

	#things = Qs.objects.all()
	things =  Qs.objects.all().filter(quote__icontains="the")

	return render(request, 'index.html',
	             {'total_count': count,
	             'things' : things,
	             })