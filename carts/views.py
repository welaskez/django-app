from django.shortcuts import render, redirect

from goods.models import Products

from carts.models import Cart

def cart_add(request, product_slug):
    """Берет продукт по его слагу, проверяет авторизован ли юзер, 
    вытаскивает все товары из корзины конкретного юзера по конкретному продукту,
    если они есть то берет самую первую, добавляет к её количеству 1 и сохраняет в бд,
    если её нет то создает новую с количеством 1 и возвращает пользователя на ту же страницу где он был"""

    product = Products.objects.get(slug=product_slug)

    if request.user.is_authenticated:
        carts = Cart.objects.filter(user=request.user, product=product)
        
        if carts.exists():
            cart = carts.first()
            if cart:
                cart.quantity += 1
                cart.save()
        else:
            Cart.objects.create(user=request.user, product=product, quantity=1)

    return redirect(request.META['HTTP_REFERER'])

def cart_change(request, product_slug):
    ...


def cart_remove(request, product_slug):
    ...
