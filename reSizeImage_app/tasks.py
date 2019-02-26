import base64
import io
from PIL import Image
from reSizeImage_project.celery import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task()
def task_resize_image(size, str_img, ext):
    name_image = task_resize_image.request.id
    bytes_img = base64.b64decode(str_img)
    logger.info('Base64 decode - SUCCESS')
    bytes_io = io.BytesIO(bytes_img)

    bytes_resised_image = io.BytesIO()
    image = Image.open(bytes_io)
    image = image.resize(size)
    if ext == 'jpg':
        ext = 'JPEG'
    image.save(bytes_resised_image, ext)
    logger.info('Save image - SUCCESS')
    bytes_resised_image = bytes_resised_image.getvalue()
    resized_str_img = base64.b64encode(bytes_resised_image).decode()
    logger.info('Base64 image encode - SUCCESS')
    return resized_str_img, name_image, ext