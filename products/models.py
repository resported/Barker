from django.db import models
from django.urls import reverse


class Product(models.Model):
    title = models.CharField('Титул', max_length=20, blank=False)
    type = models.ForeignKey('ProductType', on_delete=models.PROTECT)
    price = models.PositiveIntegerField('Цена', blank=False, null=False)
    collection = models.ForeignKey('Collection', on_delete=models.CASCADE)
    gender = models.ForeignKey('HumanGender', on_delete=models.PROTECT, default=True)
    active = models.BooleanField(default=False)
    photo = models.ImageField('Фотография', upload_to='products')
    slug = models.SlugField('Слаг', max_length=40, primary_key=True, db_index=True, blank=False, unique=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('current_product', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товар'


class ProductSize(models.Model):
    title = models.CharField(max_length=10)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Размер'
        verbose_name_plural = 'Размеры'


class ProductType(models.Model):
    title = models.CharField(max_length=40)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'


class Collection(models.Model):
    title = models.CharField('Титул', max_length=30)
    photo = models.ImageField('Фотографии', upload_to='collections')
    slug = models.SlugField('Слаг', db_index=True, primary_key=True, unique=True, blank=False)

    def __str__(self):
        return self.title

    def get_collection_url(self):
        return reverse('current_collection', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Коллекция'
        verbose_name_plural = 'Коллекции'


class HumanGender(models.Model):
    title = models.CharField('Титул', max_length=20)
    slug = models.SlugField('Слаг', unique=True, db_index=True, primary_key=True, default=True)

    def __str__(self):
        return self.title

    def get_gender_url(self):
        return reverse('current_gender', args=[str(self.slug)])

    class Meta:
        verbose_name = 'Гендер'
        verbose_name_plural = 'Гендер'
