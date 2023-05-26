from django.urls import path
from .views import ViewCoveredRegions

app_name = 'recircle_app'

urlpatterns = [
    path('view_regions/', ViewCoveredRegions.as_view(), name='view_regions'),
]
