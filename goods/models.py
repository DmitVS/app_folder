from django.db import models

class Categories(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')

    class Meta:
        db_table='category'
        verbose_name='Категория'
        verbose_name_plural='Категории'


class Products(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='Наименование')
    slug = models.SlugField(max_length=200, unique=True, blank=True, null=True, verbose_name='URL')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    image = models.ImageField(upload_to='goods_mages', blank=True, null=True, verbose_name='Изображение')
    price = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, blank=True, null=True, verbose_name='Цена')
    discount = models.DecimalField(default=0.00, max_digits=7, decimal_places=2, blank=True, null=True, verbose_name='Скидка')
    quantity = models.PositiveIntegerField(default=0, blank=True, null=True, verbose_name='Количество')
    category = models.ForeignKey(to=Categories, on_delete=models.CASCADE, verbose_name='Категория')

    class Meta:
        db_table='product'
        verbose_name='Продукт'
        verbose_name_plural='Продукты'