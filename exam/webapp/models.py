from django.db import models
from django.contrib.auth import get_user_model


category_choice = category_choice = [('laptops', 'Компьютеры'), ('keyboards', 'Клавиатура'), ('others', 'Другое'), ('mouses', 'Мышки'), ('headphones', 'Наушники')]


# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Updated At')

    class Meta:
        abstract = True

class Product(models.Model):
    name = models.CharField(blank=False, null=False, max_length=150, verbose_name='Имя')
    category = models.CharField(max_length=100, null=False, blank=False, default='others', choices=category_choice)
    description = models.TextField(max_length=2000, null=True, blank=True, verbose_name='Описание')
    pic = models.ImageField(null=True, blank=True, upload_to='user_pics', verbose_name='Картинка товара')

    class Meta:
        db_table = 'products'
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return f'{self.name} {self.category} {self.description} {self.pic}'

    
class Review(models.Model):
    product = models.ForeignKey(
        'webapp.Product',
        on_delete=models.CASCADE,
        related_name='products'
    )
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        null=True,
    )
    score = models.IntegerField(null=False, blank=False, verbose_name='Оценка')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Создано')
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Текст отзыва')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Обновлено')
    moderated = models.BooleanField(default=False)

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


