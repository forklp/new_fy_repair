from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.FyAdmin)
admin.site.register(models.FyComputer)
admin.site.register(models.FyConfig)
admin.site.register(models.FyOrder)
admin.site.register(models.FyOrderextend)
admin.site.register(models.FyRefuse)
admin.site.register(models.FyRepairlog)
admin.site.register(models.FySet)
admin.site.register(models.FyStaff)
admin.site.register(models.FyUser)
admin.site.register(models.FyUserextend)
admin.site.register(models.FyWxpush)
admin.site.register(models.FyWxuser)