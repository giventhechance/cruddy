from django.db import models


class Product(models.Model):
    title = models.CharField("Название", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=8, decimal_places=2)
    category = models.ForeignKey('Category', verbose_name='Категория', on_delete=models.CASCADE)
    shops = models.ManyToManyField('Shop', verbose_name="Магазины")

    def __str__(self):
        return self.title


class Category(models.Model):
    title = models.CharField(max_length=128)

    def __str__(self):
        return self.title


class Shop(models.Model):
    title = models.CharField(max_length=128)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.title
