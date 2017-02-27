from django.shortcuts import render
from quotations.models import Qs

# Create your views here.
def index(request):
	count = Qs.objects.count()
	things = Qs.objects.all()

	return render(request, 'index.html',
	             {'total_count': count,
	             'things' : things,
	             })

# new view
def quote_detail(request, slug):
	quote = Qs.objects.get(slug=slug)

	return render(request, 'quotes/quote_detail.html', {
		'quote': quote,
		})
