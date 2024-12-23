from django.db import models

class Users(models.Model):
    user_name = models.CharField(max_length=10)
    login = models.CharField(max_length=10)
    password = models.CharField(max_length=10)

class Tovars(models.Model):
    naimenovanie = models.CharField(max_length=255)
    vid = models.CharField(max_length=255)
    price = models.IntegerField()
    brands = models.CharField(max_length=255)

class Brands(models.Model):
    naimenovanie = models.TextField()
    vid = models.CharField(max_length=255)

class Orders(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    tovar = models.ForeignKey(Tovars, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sum = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def calculateSum(self):
        return self.tovar.price * self.quantity

    def save(self, *args, **kwargs):
        self.sum = self.calculateSum()
        super().save(*args, **kwargs)

class UserCreditCart(models.Model):
    nomer = models.CharField(max_length=16)
    cvcode = models.CharField(max_length=3)

