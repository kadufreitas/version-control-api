from rest_framework import serializers
from .. import models
from .repositorie import (
    RepositorieSerializer
)
from .environment import (
    EnvironmentSerializer
)

class ClientDetailSerializer(serializers.ModelSerializer):
    repositories = RepositorieSerializer(many=True, read_only=True)
    environments = EnvironmentSerializer(many=True, read_only=True)
    repositories_id = serializers.PrimaryKeyRelatedField(
        label='Repositório',
        source='repositories',
        queryset=models.Repositorie.objects.all(),
        write_only=True,
        many=True
    )

    class Meta:
        model = models.Client
        fields = (
            'id', 'name', 'repositories', 'repositories_id', 'environments'
        )


class ClientSerializer(serializers.ModelSerializer):
    repositories_id = serializers.PrimaryKeyRelatedField(
        read_only=False, queryset=models.Repositorie.objects.all(), source="repositories", many=True, required=False)

    class Meta:
        model = models.Client
        fields = (
            'id', 'name', 'repositories_id'
        )
