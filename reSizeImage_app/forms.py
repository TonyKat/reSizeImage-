from django.forms import ModelForm
from .models import CheckStatusTask, UploadImageModel


class CheckStatusTaskForm(ModelForm):
    class Meta:
        model = CheckStatusTask
        fields = ['text_obj']


class UploadImageForm(ModelForm):
    class Meta:
        model = UploadImageModel
        fields = ['image_obj', 'text_obj_height', 'text_obj_width']
