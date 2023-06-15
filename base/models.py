from django.contrib.auth.models import AbstractUser
from django.db import models

from common.permissions import CustomPermissions


# Create your models here.
class MyUser(AbstractUser):
    phone = models.CharField(max_length=20, default=None, null=True, blank=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.password.startswith('pbkdf2_sha256'):
            self.set_password(self.password)
        super().save(*args, **kwargs)


class AddressModel(models.Model):
    name = models.CharField(max_length=512)
    lat = models.FloatField()
    long = models.FloatField()

    class Meta:
        permissions = [
            (CustomPermissions.ADDRESS.VIEW_ADDRESS, 'Can view address'),
            (CustomPermissions.ADDRESS.CREATE_ADDRESS, 'Can create address'),
            (CustomPermissions.ADDRESS.UPDATE_ADDRESS, 'Can update address'),
            (CustomPermissions.ADDRESS.DELETE_ADDRESS, 'Can delete address'),
        ]

    def __str__(self):
        return self.name


class MediaModel(models.Model):
    images = models.ImageField(upload_to='images/')

    class Meta:
        permissions = [
            (CustomPermissions.MEDIA.VIEW_MEDIA, 'Can view media'),
            (CustomPermissions.MEDIA.CREATE_MEDIA, 'Can create media'),
            (CustomPermissions.MEDIA.UPDATE_MEDIA, 'Can update media'),
            (CustomPermissions.MEDIA.DELETE_MEDIA, 'Can delete media'),
        ]


class PitchModel(models.Model):
    name = models.CharField(max_length=200)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    address = models.ForeignKey(AddressModel, on_delete=models.CASCADE, default=None, null=True)
    price = models.IntegerField()
    imgs = models.ManyToManyField(MediaModel, blank=True)

    class Meta:
        permissions = [
            (CustomPermissions.PITCH.CREATE_PITCH, 'Can create pitch'),
            (CustomPermissions.PITCH.VIEW_PITCH, 'Can view pitch'),
            (CustomPermissions.PITCH.UPDATE_PITCH, 'Can update pitch'),
            (CustomPermissions.PITCH.DELETE_PITCH, 'Can delete pitch'),
        ]

    def __str__(self):
        return self.name


class BookingModel(models.Model):
    pitch = models.ForeignKey(PitchModel, on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    date = models.DateField()
    start = models.TimeField()
    end = models.TimeField()
    created_at = models.DateTimeField(auto_now=True)

    class Meta:
        permissions = [
            (CustomPermissions.BOOKING.CREATE_BOOKING, 'Can create booking'),
            (CustomPermissions.BOOKING.UPDATE_BOOKING, 'Can change booking'),
            (CustomPermissions.BOOKING.DELETE_BOOKING, 'Can delete booking'),
            (CustomPermissions.BOOKING.VIEW_BOOKING, 'Can get booking'),
        ]
