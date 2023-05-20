from django.shortcuts import render
from django.views.generic  import TemplateView
# Create your views here.


class AboutAsView(TemplateView):
    template_name = 'h1.html'