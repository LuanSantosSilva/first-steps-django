from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cooker.urls')),
    path('recipes/', include('cooker.urls')),
]
