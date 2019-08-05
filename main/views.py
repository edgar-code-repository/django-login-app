from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.base import TemplateView


@method_decorator(login_required, name='dispatch')
class HomePageView(TemplateView):
    template_name = "main/main_home.html"



