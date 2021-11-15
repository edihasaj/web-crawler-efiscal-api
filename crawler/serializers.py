from rest_framework.serializers import ModelSerializer

from api.models import EFiscalParams


class EFiscalSerializer(ModelSerializer):
    class Meta:
        model = EFiscalParams
        fields = 'query'
