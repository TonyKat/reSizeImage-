import io
import base64

from PIL import Image
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.safestring import mark_safe
from reSizeImage_project.settings import MEDIA_ROOT, MEDIA_URL
from .forms import CheckStatusTaskForm, UploadImageForm
from .myfunctions import read_file_bytes
from .tasks import task_resize_image
from celery.result import AsyncResult


def main_menu(request):
    return render(request, 'reSizeImage_app/main.html', {})


def resizing_image(request):
    if request.method == 'POST':
        upload_form = UploadImageForm(request.POST, request.FILES)
        if upload_form.is_valid():
            try:
                image_item = request.FILES.get('image_obj')
                width = request.POST.get('text_obj_width')
                height = request.POST.get('text_obj_height')
                size = (int(width), int(height))
                image_bytes = read_file_bytes(image_item)
                ext = image_item.name.split('.')[1]
                str_img = base64.b64encode(image_bytes).decode()
                task = task_resize_image.apply_async(args=[size, str_img, ext])

                return render(request, 'reSizeImage_app/resizing.html',
                              {'upload_form': UploadImageForm(),
                               'task_id': task.id})
            except:
                print('Ошибка в получении данных/чтении данных побитово/кодирование в base64')
                return render(request, 'reSizeImage_app/resizing.html',
                              {'upload_form': UploadImageForm(),
                               'task_id': ''})

        else:
            return render(request, 'reSizeImage_app/error_index_resize.html')
    else:
        upload_form = UploadImageForm()
    return render(request, 'reSizeImage_app/resizing.html',
                  {'upload_form': upload_form,
                   'task_id': ''})


def check_status_view(request):
    if request.method == 'POST':
        check_status_form = CheckStatusTaskForm(request.POST)
        if check_status_form.is_valid():
            try:
                text_obj = request.POST.get('text_obj')
                task = AsyncResult(text_obj)
                if task.result:
                    task_id = task.id
                    status = task.status
                    if status == 'SUCCESS':
                        bytes_task_result = base64.b64decode(task.result[0])
                        image_name = task.result[1]
                        ext = task.result[2].lower()
                        bytes_io = io.BytesIO(bytes_task_result)
                        image = Image.open(bytes_io)
                        image.save(MEDIA_ROOT + image_name + '.' + ext)
                        href = MEDIA_URL + image_name + '.' + ext
                        download_url = mark_safe('<a href="' + href + '" download>Скачать обработанное изображение</a>')
                        return render(request, 'reSizeImage_app/check_status.html',
                                      {'check_status_form': CheckStatusTaskForm(),
                                       'status': status,
                                       'task_id': task_id,
                                       'download_url': download_url})
                    return render(request, 'reSizeImage_app/check_status.html',
                                  {'check_status_form': CheckStatusTaskForm(),
                                   'status': status,
                                   'task_id': task_id,
                                   'download_url': ''})
                else:
                    return render(request, 'reSizeImage_app/error_index_check.html')
            except:
                print('Ошибка в получении данных/декодировании base64/сохранении файла на диск')
                return render(request, 'reSizeImage_app/check_status.html',
                              {'check_status_form': CheckStatusTaskForm(),
                               'status': '',
                               'task_id': '',
                               'download_url': ''})

        else:
            return HttpResponse('Invalid data')
    else:
        check_status_form = CheckStatusTaskForm()
        return render(request, 'reSizeImage_app/check_status.html',
                      {'check_status_form': check_status_form,
                       'status': '',
                       'task_id': '',
                       'download_url': ''})