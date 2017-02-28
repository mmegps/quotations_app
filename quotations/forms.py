from django.forms import ModelForm

from quotations.models import Qs

class QuoteForm(ModelForm):
	class Meta:
		model = Qs
		fields = ('date', 'quote',)