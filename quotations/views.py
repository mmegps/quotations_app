from django.shortcuts import render, redirect

from quotations.forms import QuoteForm
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

def edit_quote(request, slug):
	quote = Qs.objects.get(slug=slug)

	form_class = QuoteForm

	if request.method == 'POST':
		form = form_class(data=request.POST, instance=quote)
		if form.is_valid():
			form.save()

			return redirect('quote_detail', slug=quote.slug)
	else:
		form = form_class(instance=quote)

	return render(request, 'quotes/edit_quote.html', {
		'quote': quote,
		'form': form,
		})