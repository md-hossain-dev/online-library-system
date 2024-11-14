from rest_framework import serializers, viewsets


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth']

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['title', 'user', 'published_date','is_archived']