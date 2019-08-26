from django.contrib import admin
from uploadblock.models import file
# Register your models here.

class filelist(admin.ModelAdmin):
    list_display = ('filename',)

admin.site.register(file,filelist)