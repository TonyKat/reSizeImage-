from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^main_menu/$', views.main_menu, name='main_menu_url'),
    url(r'^resize_image/$', views.resizing_image, name='resize_image_url'),
    url(r'^check_status/$', views.check_status_view, name='check_status_url'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)