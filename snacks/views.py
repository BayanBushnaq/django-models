from django.shortcuts import render
from django.views.generic import TemplateView , ListView , DetailView
from .models import Snack
class HomePage(TemplateView):
    template_name = 'home.html'

class SnacksListView(ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetails(DetailView):
    model = Snack
    template_name = 'snack_details.html'
