from datetime import datetime, timedelta

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.response import Response

from common.permissions import RoleBasedPermission, CustomPermissions
from . import models, serializers, filters


# Create your views here.
class PitchViewset(viewsets.ModelViewSet):
    permission_classes = (RoleBasedPermission,)

    permission_codes = {
        'GET': CustomPermissions.PITCH.META.VIEW_PITCH,
        'POST': CustomPermissions.PITCH.META.CREATE_PITCH,
        'PUT': CustomPermissions.PITCH.META.UPDATE_PITCH,
        'PATCH': CustomPermissions.PITCH.META.UPDATE_PITCH,
        'DELETE': CustomPermissions.PITCH.META.DELETE_PITCH,
    }

    queryset = models.PitchModel.objects.all()
    serializer_class = serializers.PitchSerializer
    filter_backends = (DjangoFilterBackend,)
    filterset_class = filters.PitchFilter

    def list(self, request, *args, **kwargs):
        date = self.request.query_params.get('date', datetime.now().strftime('%Y-%m-%d'))
        start_time = self.request.query_params.get('start_time', datetime.now().strftime('%H:%M:%S'))
        end_time = self.request.query_params.get('end_time', (datetime.now() + timedelta(hours=2)).strftime('%H:%M:%S'))
        lat = self.request.query_params.get('lat')
        long = self.request.query_params.get('long')

        query = '''
            SELECT 
                pitch.id,
                pitch.name,
                address.name as address_name,
                trunc(SQRT(pow({lat}-lat, 2) + pow({long}-long, 2))::numeric, 3) as distance,
                pitch.price,
                CASE
                    WHEN booking.user_id IS NULL THEN true
                    ELSE false
                END as is_free
            FROM 
                base_pitchmodel as pitch
            LEFT JOIN
                base_addressmodel as address
            ON
                address.id=pitch.address_id
            LEFT JOIN
                base_bookingmodel as booking
            ON 
                (booking.pitch_id=pitch.id and booking.date='{date}') and not (booking.end<='{start_time}' or booking.start>='{end_time}')
            ORDER BY
                distance
        '''.format(lat=lat, long=long, date=date, start_time=start_time, end_time=end_time)

        data = models.PitchModel.objects.raw(query)
        valid_data = serializers.GetFreePitchSerializer(data, many=True)
        return Response(valid_data.data)

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return serializers.GetFreePitchSerializer
        return super().get_serializer_class()
