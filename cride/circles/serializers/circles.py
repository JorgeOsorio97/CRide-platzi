"""Circle serializers."""

# Django REST Framework
from rest_framework import serializers

# Model
from cride.circles.models import Circle

class CircleModelSerializer(serializers.ModelSerializer):
    """Circle Model Serializer."""

    members_limit = serializers.IntegerField(
        required=False,
        min_value=10,
        max_value=32000
    )
    is_limited = serializers.BooleanField(default=False)

    class Meta:
        """Meta class."""

        model = Circle
        fields = (
            'name', 'slug_name',
            'about', 'picture',
            'rides_offered', 'rides_taken',
            'verified', 'is_public',
            'is_limited', 'members_limit'
        )
        read_only_fields = (
            'is_public',
            'verified',
            'rides_offered',
            'rides_taken'
        )

    def validate(self, data):
        """Ensure both members limit and is limited are present."""
        memebers_limit = data.get('members_limit', None)
        is_limited = data.get('is_limited', False)
        if bool(memebers_limit) ^ is_limited:
            raise serializers.ValidationError('If circles is limited, a member limit must be provided')
        return data