# Generated by Django 4.2.4 on 2023-08-26 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flower_app', '0003_category_bouquet_categories'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Повод', 'verbose_name_plural': 'Поводы'},
        ),
        migrations.AlterField(
            model_name='bouquet',
            name='composition',
            field=models.ManyToManyField(blank=True, to='flower_app.composition'),
        ),
    ]
