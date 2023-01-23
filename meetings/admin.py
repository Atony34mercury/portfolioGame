from django.contrib import admin

from .models import Meeting,Room

admin.site.register([Meeting,Room])
