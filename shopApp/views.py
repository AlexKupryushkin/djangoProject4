from django.shortcuts import render, get_object_or_404
from .models import *
from django.views import View
from shopApp.models import Products
import datetime


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
    uuid_user = request.POST.get('uuid', False)
    el_ticket = Tickets(uuid=uuid_user)
    el = get_object_or_404(Tickets, id=1)

    # if el_ticket == el:
    #     return render(request, 'base.html')

    # # el_ticket = Tickets(uuid=uuid)
    # if uuid == Tickets.uuid:
    #     el_ticket.save()
    # else:
    return render(request, "./tickets.html",
                  {'title': 'Тикеты', 'uuid': uuid_user}
                  )


def thanks_page(request):
    name = request.POST['name']
    password = request.POST['password']
    points = request.POST['points']
    element = Users(username=name, password=password, points=points)
    # element.save()
    return render(request, "./thanks_page.html",
                  {'name': name, 'password': password, 'points': points}
                  )


def exchange(request):
    return render(request, "exchange.html")


def add_to_basket(request, prod_id):
    product_id = Products.objects.get(pk=prod_id)
    Orders.objects.create(user_id=request.user, product_id=product_id, count=1, order_datetime=datetime.datetime.now())
    return render(request,  "basket.html")


class Enter(View):

    def get(self, request):
        # all_posts = Products.objects.all()
        return render(request, "enter.html", {'title': 'Войти'}
                      # {"products": all_posts}
                      )
