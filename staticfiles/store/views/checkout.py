from django.shortcuts import render, redirect

from django.contrib.auth.hashers import check_password

from store.models.customer import Customer
from django.views import View
from store.models.product import Product
from store.models.orders import Order


class CheckOut(View):
    def post(self, request):
        name = request.POST.get('name')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        customer = request.session.get('customer')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        product_name = Product.name
        print(name, address, phone, customer, cart, products, product_name)

        for product in products:
            print(cart.get(str(product.id)))
            order = Order(customer=Customer(id=customer),
                          product=product,
                          product_name=product.name,
                          price=product.price,
                          name=name,
                          address=address,
                          phone=phone,
                          quantity=cart.get(str(product.id)))
            order.save()
        request.session['cart'] = {}

        return redirect('cart')
