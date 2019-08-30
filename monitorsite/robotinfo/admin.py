from django.contrib import admin

# Register your models here.  在admin管理界面管理ytrbts表
from robotinfo.models import ytrbts

admin.site.register(ytrbts)