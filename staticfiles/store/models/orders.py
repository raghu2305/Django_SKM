from django.db import models
from .product import Product
from .customer import Customer
import datetime

class Order(models.Model):
    product = models.ForeignKey(Product , on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer , on_delete=models.CASCADE)
    product_name = models.CharField(default='' , max_length=100)
    quantity = models.IntegerField(default=1)
    price = models.IntegerField()
    name = models.CharField(max_length=50 , default='')
    address = models.CharField(max_length=500 , default='')
    phone = models.CharField(max_length=15 , default='')
    date = models.DateField(default=datetime.datetime.today)
    time = models.TimeField(default=datetime.datetime.now)
    status = models.BooleanField(default=False)


    def placeOrder(self):
        self.save()

    @staticmethod
    def get_orders_by_customer(customer_id):
        return Order.objects.filter(customer = customer_id).order_by('-date' and 'time')