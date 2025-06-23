from django.contrib import admin

from .models import Deliverer, Record

admin.site.register(Record)
admin.site.register(Deliverer)