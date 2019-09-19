from rest_framework import serializers
from .. import models
from .tag import TagsSerializer

class EnvironmentDetailSerializer(serializers.ModelSerializer):
    client = serializers.StringRelatedField()
    tags = TagsSerializer(read_only=True, many=True)
    tags_id = serializers.PrimaryKeyRelatedField(
        queryset=models.Tag.objects.all(),
        source='tags',
        write_only=True,
        many=True
    )

    class Meta:
        model = models.Environment
        fields = (
            'id', 'name', 'client', 'tags', 'tags_id'
        )


class EnvironmentSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='version_control:environments-detail', format='html', lookup_field='pk')
    tags_id = serializers.PrimaryKeyRelatedField(
        write_only=True, 
        queryset=models.Tag.objects.all(),
        source="tags", 
        many=True,
        required=False
    )
    tags = TagsSerializer(read_only=True, many=True)
    class Meta:
        model = models.Environment
        fields = (
            'id', 'url', 'name', 'client', 'tags_id', 'tags'
        )
