from rest_framework import serializers

from apps.otc.models import OtcBase


class OTCSerializer(serializers.ModelSerializer):

    class Meta:
        model = OtcBase
        fields = (
            'otc',
            'created_in',
            'is_used',
            'used_in',
            'user'
        )
