from django.shortcuts import get_object_or_404

from rest_framework import viewsets, response, mixins
from rest_framework.decorators import action
from . import models, serializers
# Create your views here.


class ClientsViewSet(viewsets.ModelViewSet):
    queryset = models.Client.objects.all()
    serializer_class = serializers.client.ClientSerializer

    def get_serializer_class(self):
        if self.detail:
            return serializers.ClientDetailSerializer
        else:
            return serializers.ClientSerializer


class RepositoriesViewSet(viewsets.ModelViewSet):
    queryset = models.Repositorie.objects.all()
    serializer_class = serializers.RepositorieSerializer


class TagsViewSet(viewsets.ModelViewSet):
    queryset = models.Tag.objects.all()
    serializer_class = serializers.TagsSerializer

    def get_serializer_class(self):
        if self.detail:
            return serializers.TagsSerializer
        else:
            return serializers.TagsAddSerializer


class EnvironmentsViewSet(viewsets.ModelViewSet):
    queryset = models.Environment.objects.all()
    serializer_class = serializers.EnvironmentSerializer

    def get_serializer_class(self):
        if self.detail:
            return serializers.EnvironmentDetailSerializer
        else:
            return serializers.EnvironmentSerializer
