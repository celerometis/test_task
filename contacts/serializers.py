from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.ModelSerializer):
    full_name = serializers.SerializerMethodField(read_only=True)
    update_time = serializers.DateTimeField(source='updated_at',
                                            read_only=True)

    class Meta:
        model = Contact
        fields = [
            'first_name',
            'last_name',
            'phone',
            'email',
            'full_name',
            'update_time'
        ]

    def get_full_name(self, obj):
        if not hasattr(obj, 'id'):
            return None
        return obj.full_name

    def validate_first_name(self, value):
        qs = Contact.objects.filter(first_name__exact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already exists")
        return True
