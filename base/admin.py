from django.contrib import admin
from django.contrib.auth.models import Permission
from . import models


# Register your models here.
@admin.register(Permission)
class PermissionAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.MyUser)
admin.site.register(models.PitchModel)
admin.site.register(models.AddressModel)
admin.site.register(models.BookingModel)
