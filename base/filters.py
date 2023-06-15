from django_filters import filters, FilterSet
from . import models


class PitchFilter(FilterSet):
    class Meta:
        model = models.PitchModel
        fields = '__all__'
