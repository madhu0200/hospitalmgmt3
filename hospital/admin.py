from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register(register_doctor)
admin.site.register(blogs)
admin.site.register(appointments)