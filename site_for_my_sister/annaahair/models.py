from django.db import models

# Create your models here.
class Annaahair(models.Model):
    title = models.CharField('Заголовок:', max_length=100)
    review = models.TextField('Текст:')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Информация'
        ordering = ['-title']

class Annaahair_review(models.Model):
    title1 = models.CharField('Имя пользователя:', max_length=100)
    review1 = models.TextField('Комментарий:')

    def __str__(self):
        return self.title1

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-title1']

