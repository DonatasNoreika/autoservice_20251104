from django.db import models


class Service(models.Model):
    name = models.CharField()
    price = models.FloatField()

    def __str__(self):
        return self.name

class Car(models.Model):
    make = models.CharField()
    model = models.CharField()
    license_plate = models.CharField(max_length=10)
    vin_code = models.CharField(max_length=20)
    client_name = models.CharField()

    def __str__(self):
        return f"{self.make} {self.model}"


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(to="Car", on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.car} ({self.date})"

class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE)
    service = models.ForeignKey(to="Service", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()

    def __str__(self):
        return f"{self.service} - {self.quantity}"
