from django.db import models
from reSizeImage_app.myfunctions import validate_file_extension
from django.core.validators import MaxValueValidator, MinValueValidator


class CheckStatusTask(models.Model):
    text_obj = models.CharField(verbose_name='Введите идентификатор:', max_length=40)


class UploadImageModel(models.Model):
    image_obj = models.ImageField(verbose_name='Загрузка файла',
                                  validators=[validate_file_extension])
    text_obj_width = models.IntegerField(verbose_name='Ширина:', validators=[MinValueValidator(1),
                                                                             MaxValueValidator(9999)], blank=False)
    text_obj_height = models.IntegerField(verbose_name='Высота:', validators=[MinValueValidator(1),
                                                                              MaxValueValidator(9999)], blank=False)
