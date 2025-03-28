from AppVehiculos.models import vehiculo
from rest_framework import serializers

class vehiculo_serializer(serializers.ModelSerializer):
    class Meta:
        model=vehiculo
        fields=['id','placa','marca','color','modelo']
        