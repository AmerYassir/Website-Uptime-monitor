from django.contrib import admin
from .models import Website, HealthCheck

admin.site.register(Website)
admin.site.register(HealthCheck)