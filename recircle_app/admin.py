from django.contrib import admin

from recircle_app.models import StateStats

# Registering the StateStats Model to Access/View Data at Admin Side
admin.site.register(StateStats)
