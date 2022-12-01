from django.urls import path
from .views import HomeListView, ShowListView
from . import views

urlpatterns =[
    path('',HomeListView.as_view(), name='table-home'),
    path('show/<str:show_id>/', ShowListView.as_view(), name='table-show'),
]

