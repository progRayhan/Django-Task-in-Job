from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    amount = models.IntegerField()
    category = models.ForeignKey(Category, null=False, on_delete=models.CASCADE)

    def discount_price (self):
        if self.amount == 10:
            price1 = self.price
            price2 = (price1*10) - (price1*0.5)
        elif self.amount != 10:
            price2 = 0
        return price2

    def total_price(self):
        t_price = self.price*self.amount
        return t_price
    
    def save_price(self):
        a = (self.price*10) - (self.price*0.5)
        if self.amount == 10:
            s_price = (self.price*self.amount) - a
            return s_price

    def __str__(self):
        return self.name