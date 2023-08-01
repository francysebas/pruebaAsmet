from .models import Persona, Caso, TipoPersona,TipoDocumento, Juzgado

from rest_framework import serializers


class TipoPerSerializer(serializers.ModelSerializer):

    class Meta:
        model= TipoPersona
        fields = ['nombre']


class TipoDocSerializer(serializers.ModelSerializer):

    class Meta:
        model= TipoDocumento
        fields = ['nombre']


class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Persona
        fields = '__all__'

    def to_representation(self, instance):
        return {
        'identificacion' : instance.identificacion,
        'tipoIdentificacion' : instance.tipoIdentificacion.nombre,
        'nombres' : instance.nombres,
        'apelllidos' : instance.apelllidos,
        'fechaNaciemiensto' : instance.fechaNaciemiensto,
        'ciudadResidencia' : instance.ciudadResidencia,
        'direccion' : instance.direccion,
        'telefono' : instance.telefono,
        'celular':instance.celular,
        'tipoPersona' :instance.tipoPersona.nombre,
        }


class CasoSerializer(serializers.ModelSerializer):

    class Meta:
        model= Caso
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'NumeroCaso' :instance.NumeroCaso,
            'NombrePersona' : instance.IdPersona.apelllidos,
            'ApellidoPersona': instance.IdPersona.nombres,
            'IdenPersona': instance.IdPersona.identificacion,
            'IdJuzgado' : instance.IdJuzgado.nombre,
        }


class JuzgadoSerializer(serializers.ModelSerializer):
    class Meta:
        model= Juzgado
        fields = '__all__'
