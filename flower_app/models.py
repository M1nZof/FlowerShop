from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Composition(models.Model):
    name = models.CharField('Компонент', max_length=30)

    class Meta:
        verbose_name = 'компонент'
        verbose_name_plural = 'компоненты'

    def __str__(self):
        return self.name


class Bouquet(models.Model):
    name = models.CharField('Название', max_length=50)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    image = models.ImageField('Картинка')
    composition = models.ManyToManyField(Composition, blank=True)
    height = models.IntegerField('Высота в сантиметрах')
    width = models.IntegerField('Ширина в сантиметрах')
    categories = models.ManyToManyField('Category', verbose_name='Для каких поводов', related_name='bouquets')
    description = models.TextField('Описание')

    class Meta:
        verbose_name = 'букет'
        verbose_name_plural = 'букеты'

    def __str__(self):
        return f'{self.name}, {self.price} руб.'


class CompositionSet(models.Model):
    composition = models.ForeignKey(Composition, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField('Количество', default=1)
    bouquet = models.ForeignKey(Bouquet, on_delete=models.PROTECT)


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
        return f'{self.name} | {self.phone_number} | {self.time}'


class Order(models.Model):
    name = models.CharField('Имя клиента', max_length=50)
    phone_number = PhoneNumberField(region='RU', verbose_name='Телефон клиента')
    address = models.CharField('Адрес доставки', max_length=100)
    time = models.TimeField('Время доставки', blank=True, null=True)
    email = models.EmailField('Почта клиента', blank=True, null=True)

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'

    def __str__(self):
        return f'{self.name} | {self.phone_number} | {self.address} | {self.email}'


class Category(models.Model):
    title = models.CharField('Повод', max_length=50)

    class Meta:
        verbose_name = 'Повод'
        verbose_name_plural = 'Поводы'

    def __str__(self):
        return self.title
