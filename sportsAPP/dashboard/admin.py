from django.contrib import admin
from .models import Datas

# Register your models here.

class DatasAdmin(admin.ModelAdmin):
    list_display = ('name','age','height','sex','prediction')
admin.site.register(Datas,DatasAdmin)