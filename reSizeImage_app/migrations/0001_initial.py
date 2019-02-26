# Generated by Django 2.1.1 on 2019-02-26 15:40

import django.core.validators
from django.db import migrations, models
import reSizeImage_app.myfunctions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CheckStatusTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text_obj', models.CharField(max_length=40, verbose_name='Введите идентификатор:')),
            ],
        ),
        migrations.CreateModel(
            name='UploadImageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_obj', models.ImageField(upload_to='', validators=[reSizeImage_app.myfunctions.validate_file_extension], verbose_name='Загрузка файла')),
                ('text_obj_width', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)], verbose_name='Ширина:')),
                ('text_obj_height', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(9999)], verbose_name='Высота:')),
            ],
        ),
    ]
