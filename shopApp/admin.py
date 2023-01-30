from django.contrib import admin

# Register your models here.from django.contrib import admin
from shopApp.models import Products
from shopApp.models import Users
from shopApp.models import Orders
from shopApp.models import Tickets
#
admin.site.register(Products)
admin.site.register(Users)
admin.site.register(Orders)
admin.site.register(Tickets)

