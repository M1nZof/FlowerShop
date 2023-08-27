from django import forms
from .models import Order, Consultation


class OrderForm(forms.ModelForm):
    DELIVERY_TIME = [
        ('ASAP', 'Как можно скорее'),
        ('FROM_10_TO_12', 'С 10:00 до 12:00'),
        ('FROM_12_TO_14', 'С 12:00 до 14:00'),
        ('FROM_14_TO_16', 'С 14:00 до 16:00'),
        ('FROM_16_TO_18', 'С 16:00 до 18:00'),
        ('FROM_18_TO_20', 'С 18:00 до 20:00'),
    ]

    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Введите Имя',
                                                         'class': "order__form_input"}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': '+7(777)7777777',
                                                                 'class': "order__form_input"}))
    address = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Адрес доставки',
                                                            'class': "order__form_input"}))
    time = forms.ChoiceField(choices=DELIVERY_TIME, widget=forms.RadioSelect(attrs={'class': "order__form_radio" }))

    class Meta:
        model = Order
        fields = ['name', 'phone_number', 'address', 'time', 'email']
