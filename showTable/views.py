from django.shortcuts import render
from django.views.generic import ListView
from django.db.models.functions import Lower
from .models import Episodes, Shows
# Create your views here.

class HomeListView(ListView):
    model = Shows
    template_name = 'showTable/home.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        temp = Shows.objects.using('showData').order_by(Lower('show_title'))
        context['eps'] = temp
        return context


class ShowListView(ListView):
    model = Episodes
    template_name = 'showTable/showDetail.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['eps'] = Episodes.objects.using('allEpisodes').order_by(
            'season_number','season_title').filter(show_url=self.kwargs['show_id'])
        return context

