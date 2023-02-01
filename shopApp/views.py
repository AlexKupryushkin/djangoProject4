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
    uuid = request.POST.get('uuid', False)
    el_ticket = Tickets(uuid=uuid)
    if uuid == Tickets.uuid:
        el_ticket.save()
    else:
        return render(request, "./tickets.html",
                      {'title': 'Тикеты', 'uuid': uuid}
                      )


def thanks_page(request):
    name = request.POST['name']
    password = request.POST['password']
    points = request.POST['points']
    element = Users(username=name, password=password, points=points)
    element.save()
    return render(request, "./thanks_page.html",
                  {'name': name, 'password': password, 'points': points}
                  )


def exchange(request):
    return render(request, "exchange.html")


class Enter(View):

    def get(self, request):
        # all_posts = Products.objects.all()
        return render(request, "enter.html", {'title': 'Войти'}
                      # {"products": all_posts}
                      )
