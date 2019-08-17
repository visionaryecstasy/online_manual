from django.contrib import admin
from .models import Manual
from .models import Message
from .models import comment

# Register your models here.
admin.site.register(Manual)
admin.site.register(Message)
admin.site.register(comment)