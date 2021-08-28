from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("index.urls"), name="index"),
    path('accounts/', include("accounts.urls"), name="accounts"),
]
