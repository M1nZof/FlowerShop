from django.db import models
from tinymce.models import HTMLField
from phonenumber_field.modelfields import PhoneNumberField


class Bouquet(models.Model):
    name = models.CharField('Название', max_length=50)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Картинка')
    composition = HTMLField('Состав')
    height = models.IntegerField('Высота')
    width = models.DecimalField('Ширина', max_digits=10, decimal_places=1)
    # categories = models.ForeignKey(Category, ..., )       # Не уверен, что нужно будет, но фигурирует в quiz.html
    description = HTMLField('Описание')

    class Meta:
        verbose_name = 'букет'
        verbose_name_plural = 'букеты'

    def __str__(self):
        return f'{self.name}, {self.price} руб.'


class Place(models.Model):
    address = models.CharField('Адрес', max_length=100)
    phone_number = PhoneNumberField(region='RU', verbose_name='Телефон')
    image = models.ImageField('Картинка')

    class Meta:
        verbose_name = 'торговая точка'
        verbose_name_plural = 'торговые точки'

    def __str__(self):
        return self.address


class Consultation(models.Model):
    name = models.CharField('Имя клиента', max_length=50)
    phone_number = PhoneNumberField(region='RU', verbose_name='Телефон клиента')
    time = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'консультация'
        verbose_name_plural = 'консультации'

    def __str__(self):
        return f'{self.name} | {self.time}'


class Order(models.Model):
    name = models.CharField('Имя клиента', max_length=50)
    phone_number = PhoneNumberField(region='RU', verbose_name='Телефон клиента')
    address = models.CharField('Адрес доставки', max_length=100, blank=True, null=True)  # null+blank для самовывоза
    time = models.TimeField('Время доставки', blank=True, null=True)                     # аналогично
    email = models.EmailField('Почта клиента', blank=True, null=True)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'{self.name} | {self.phone_number} | {self.address} | {self.email}'
