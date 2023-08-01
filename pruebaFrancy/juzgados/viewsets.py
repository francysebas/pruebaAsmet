from rest_framework import viewsets
from rest_framework import filters
from .models import Caso,Persona, Juzgado, TipoPersona, TipoDocumento

from .serializalizer import PersonaSerializer, CasoSerializer, JuzgadoSerializer, TipoPerSerializer, TipoDocSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset =  Persona.objects.all()
    serializer_class = PersonaSerializer


class JuzgadoViewSet(viewsets.ModelViewSet):
    queryset = Juzgado.objects.all()
    serializer_class = JuzgadoSerializer


class CasoViewSet(viewsets.ModelViewSet):
    queryset = Caso.objects.all()
    serializer_class = CasoSerializer


class TipoPerViewSet(viewsets.ModelViewSet):
    queryset = TipoPersona.objects.all()
    serializer_class = TipoPerSerializer


class TipoDocViewSet(viewsets.ModelViewSet):
    queryset = TipoDocumento.objects.all()
    serializer_class = TipoDocSerializer