from django.contrib import admin
from django.urls import path

from speech_api.views import english_asr, rus_asr

urlpatterns = [
    path("admin/", admin.site.urls),
    path("/api/upload/eng", english_asr),
    path("/api/upload/rus", rus_asr),
]
