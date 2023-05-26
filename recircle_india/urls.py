from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recircle_app/', include('recircle_app.urls', namespace='recircle')),
]
