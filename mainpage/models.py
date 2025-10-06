from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_delete

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок") # verbos
    text = models.TextField(verbose_name="Текст")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        db_table = "blog_posts"

    def __str__(self):
        return self.title

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="Заголовок") # verbos
    text = models.TextField(verbose_name="Текст")
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name = "Проект"
        verbose_name_plural = "Проекты"
        db_table = "desing_project"

    def __str__(self):
        return self.title


class ProjectFile(models.Model):
    name = models.CharField(max_length=20)
    # Поле image будет сохранять файлы в папку 'uploads' внутри MEDIA_ROOT
    text = models.TextField(verbose_name="Текст")
    related_name='images' 
    file = models.FileField(upload_to='uploads/')
    desing_project = models.ForeignKey(Project, on_delete=models.CASCADE)
    class Meta:
        verbose_name = "Медиа проекта"
        verbose_name_plural = "Медиа проектов"
        db_table = "media_desing_project"
    def __str__(self):
        return self.name
    
@receiver(pre_delete, sender=ProjectFile)
def delete_model_image(sender, instance, **kwargs):
    if instance.file:
        # Удаляем файл с диска
        instance.file.delete(save=False)