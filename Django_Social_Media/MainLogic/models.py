from django.db import models

# Create your models here.

class AddPost(models.Model):
    title = models.CharField(max_length=40, verbose_name='Назва Аккаунта')
    image = models.ImageField(verbose_name='Зображення')
    full_text = models.TextField(verbose_name='Опис')


    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Добавити пост'
        verbose_name_plural = 'Добавити пости'
    
    