import os
from django.core.exceptions import ValidationError


def read_file_bytes(instance):
    instance.open()
    instance.seek(0)
    file = b''
    for chunk in iter(lambda: instance.read(4096), b''):
        file += chunk
    return file


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Неподдерживаемое расширение файла.')
