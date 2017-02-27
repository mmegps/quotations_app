from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView

from quotations import views

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^about',
    	TemplateView.as_view(template_name='about.html'),
    	name='about'),
    url(r'^contact', 
        TemplateView.as_view(template_name='contact.html'),
        name='contact'),
    url(r'^quotes/(?P<slug>[-\w]+)/$', views.quote_detail,
    	name='quote_detail'),
    url(r'^admin/', admin.site.urls),
]
