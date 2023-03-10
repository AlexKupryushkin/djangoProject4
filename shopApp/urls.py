from django.http import request
from . import views
from django.urls import path
from django.views.generic import TemplateView
from .views import *

urlpatterns = [
    path("", TemplateView.as_view(template_name="base.html")),


    path('products', products, name='products'),

    path('enter/tickets', tickets, name='tickets'),


    path('enter', views.Enter.as_view(), name="enter"),
    path('enter/users', profile, name='users'),
    path('thanks', views.thanks_page, name='thanks'),
    path('exchange', views.exchange, name='exchange'),
    path('basket', views.add_to_basket, name='basket'),

]