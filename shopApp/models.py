from django.db import models
import pathlib
import uuid


class Users(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    points = models.IntegerField()


class Tickets(models.Model):
    uuid = models.CharField(max_length=36)
    available = models.BooleanField(default=True)
    user_id = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.uuid


class Products(models.Model):
    name = models.CharField(max_length=255, null=False)
    cost = models.SmallIntegerField()
    count = models.SmallIntegerField()

    def __str__(self):
        return self.name


class Orders(models.Model):
    user_id = models.ForeignKey(Users, on_delete=models.SET_NULL, null=True)
    product_id = models.ForeignKey(Products, on_delete=models.SET_NULL, null=True)
    count = models.SmallIntegerField()
    order_datetime = models.DateTimeField()


