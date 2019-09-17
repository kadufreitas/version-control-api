from rest_framework import serializers
from .. import models


class RepositorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Repositorie
        fields = (
            'id', 'name'
        )