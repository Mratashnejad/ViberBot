from django.contrib import admin
from django.urls import path
from myviberBot.views import trx_bot
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('webhook2020', trx_bot),
]


