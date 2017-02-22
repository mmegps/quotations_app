from django.contrib import admin

#import your model
from quotations.models import Qs

# set up automated slug creation
class QsAdmin(admin.ModelAdmin):
	model = Qs
	list_display = ('quote', 'date',)
	prepopulated_fields = {'slug': ('quote',)}

#register it
admin.site.register(Qs, QsAdmin)