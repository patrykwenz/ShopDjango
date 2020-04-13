from django.db import models
from django.shortcuts import reverse

# Create your models here.

QUALITY_CHOICE = (
    ('PR', 'Premium'),
    ('BS', 'Basic')
)


class Item(models.Model):
    title = models.CharField(max_length=150)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    quality = models.CharField(max_length=30, choices=QUALITY_CHOICE)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('products:product', args=[str(self.id)])

    def get_to_cart_url(self):
        return reverse('products:add-to-cart', args=[str(self.id)])

    def get_remove_cart_url(self):
        return reverse('products:remove-from-cart', args=[str(self.id)])


class OrderItem(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    ordered = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.quantity} || {self.item.title}"

    def get_total_item_price(self):
        return self.quantity * self.item.price

    def get_total_discount_item_price(self):
        return self.quantity * self.item.discount_price

    def get_amount_saved(self):
        return self.get_total_item_price() - self.get_total_discount_item_price()

    def get_final_price(self):
        if self.item.discount_price:
            return self.get_total_discount_item_price()
        return self.get_total_item_price()


class Order(models.Model):
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    ordered = models.BooleanField(default=False)
    start_date = models.DateTimeField(auto_now_add=True)
    ordered_date = models.DateTimeField()

    # def __str__(self):
    #     return self.title

    def get_total(self):
        # total = 0
        # for order_item in self.items.all():
            # total += order_item.get_final_price()
        # if self.coupon:
        #     total -= self.coupon.amount
        return sum([item.get_final_price() for item in self.items.all()])
