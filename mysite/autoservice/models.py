from django.utils import timezone
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField

class Service(models.Model):
    name = models.CharField()
    price = models.FloatField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Service"
        verbose_name_plural = "Services"

class Car(models.Model):
    make = models.CharField()
    model = models.CharField()
    license_plate = models.CharField(max_length=10)
    vin_code = models.CharField(max_length=20)
    client_name = models.CharField()
    photo = models.ImageField(upload_to="cars", null=True, blank=True)
    description = HTMLField(default="")

    def __str__(self):
        return f"{self.make} {self.model}"

    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"


class Order(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    car = models.ForeignKey(to="Car", on_delete=models.SET_NULL, null=True, blank=True)
    client = models.ForeignKey(to=User, on_delete=models.CASCADE)

    LOAN_STATUS = (
        ('c', "Confirmed"),
        ('i', 'In Progress'),
        ('o', 'Completed'),
        ('e', 'Canceled'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='c')
    deadline = models.DateTimeField(null=True, blank=True)

    def total(self):
        result = 0
        for line in self.lines.all():
            result += line.line_sum()
        return result

    def is_overdue(self):
        return self.deadline and self.deadline < timezone.now()

    def __str__(self):
        return f"{self.car} ({self.date})"

    class Meta:
        verbose_name = "Order"
        verbose_name_plural = "Order"

class OrderLine(models.Model):
    order = models.ForeignKey(to="Order", on_delete=models.CASCADE, related_name='lines')
    service = models.ForeignKey(to="Service", on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField()

    def line_sum(self):
        return self.service.price * self.quantity

    def __str__(self):
        return f"{self.service} - {self.quantity}"

    class Meta:
        verbose_name = "Order line"
        verbose_name_plural = "Order lines"


class OrderComment(models.Model):
    order = models.ForeignKey(to="Order",
                              on_delete=models.SET_NULL,
                              null=True, blank=True,
                             related_name="comments")
    author = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    date_created = models.DateTimeField(verbose_name="Date Created", auto_now_add=True)
    content = models.TextField(verbose_name="Content")