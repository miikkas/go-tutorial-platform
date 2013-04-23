from django.contrib import admin
from goviewer.models import *

class MyModelAdmin(admin.ModelAdmin):
    pass

admin.site.register(MyModel, MyModelAdmin)
