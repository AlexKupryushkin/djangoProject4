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



# def user_page(request):
#     object_list = O


def thanks_page(request):
    name = request.POST['name']
    password = request.POST['password']
    points = request.POST['points']
    element = Users(username=name, password=password, points=points)
    element.save()
    return render(request, "./thanks_page.html",
                  {'name': name, 'password': password, 'points': points}
                  )


class Enter(View):

    def get(self, request):
        # all_posts = Products.objects.all()
        return render(request, "enter.html", {'title': 'Войти'}
                      # {"products": all_posts}
                      )
