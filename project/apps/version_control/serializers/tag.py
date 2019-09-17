from rest_framework import serializers
from .. import models


class TagsSerializer(serializers.ModelSerializer):
    repositorie = serializers.StringRelatedField()
    
    class Meta:
        model = models.Tag
        fields = (
            'id', 'name', 'repositorie'
        )
