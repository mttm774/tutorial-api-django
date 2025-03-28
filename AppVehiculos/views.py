import json
from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status,permissions
from AppVehiculos.models import vehiculo
from .serializers import vehiculo_serializer

class VehiculoApiView(APIView):

    def post(self, request, *args,**kwargs):
        data={
            'placa':request.data.get('placa'),
            'marca':request.data.get('marca'),
            'color':request.data.get('color'),
            'modelo':request.data.get('modelo'),
            }
        serializador=vehiculo_serializer(data=data)
        if serializador.is_valid():
            serializador.save()
            return Response(serializador.data, status=status.HTTP_201_CREATED)
        
        return Response(serializador.data, status=status.HTTP_400_BAD_REQUEST)
    
    def get(self,request,*args, **kwargs):
        lista_vehiculos=vehiculo.objects.all()
        serializer_vehiculos=vehiculo_serializer(lista_vehiculos,many=True)
        return Response(serializer_vehiculos.data, status=status.HTTP_200_OK)
    
    def put(self, request, pkid):
        mivehiculo=vehiculo.objects.filter(id=pkid).update(
            placa=request.data.get('placa'),
            marca=request.data.get('marca'),
            color=request.data.get('color'),
            modelo=request.data.get('modelo')
        )
        return Response(mivehiculo, status=status.HTTP_200_OK)
   


    def delete(self, request, pkid, *args, **kwargs):
        try:
            mivehiculo = vehiculo.objects.get(id=pkid)
            mivehiculo.delete()
            return Response({"message": "Vehículo eliminado exitosamente."}, status=status.HTTP_204_NO_CONTENT)
        except vehiculo.DoesNotExist:
            return Response({"error": "Vehículo no encontrado."}, status=status.HTTP_404_NOT_FOUND)
