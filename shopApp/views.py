from django.shortcuts import render
from .models import *
from django.views import View

from shopApp.models import Products


# def products_show(request):
#         return render(request, "base.html")

def products(request):
    posts = Products.objects.all()
    return render(request, "products.html",
                  {'title': 'Продукты', 'posts': posts}
              )



def profile(request):
    user = Users.objects.all()
    return render(request, "users.html", {'title': 'Пользователь', 'user': user})


def tickets(request):
    ticket = Tickets.objects.all()
    return render(request, "tickets.html", {'title': 'Тикеты', 'ticket': ticket})




class Enter(View):

    def get(self, request):
        # all_posts = Products.objects.all()
        return render(request, "enter.html", {'title': 'Войти'}
                      # {"products": all_posts}
                      )
