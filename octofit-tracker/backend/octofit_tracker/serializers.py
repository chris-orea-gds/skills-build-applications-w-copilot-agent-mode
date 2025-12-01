from rest_framework import serializers
from django.contrib.auth.models import User

# Serializador para el usuario
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

# Serializador para equipos
class TeamSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    name = serializers.CharField(max_length=100)
    members = UserSerializer(many=True, read_only=True)

# Serializador para actividades
class ActivitySerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)
    type = serializers.CharField(max_length=100)
    duration = serializers.IntegerField()
    date = serializers.DateField()

# Serializador para el leaderboard
class LeaderboardSerializer(serializers.Serializer):
    user = UserSerializer(read_only=True)
    total_duration = serializers.IntegerField()

# Serializador para sugerencias de entrenamiento
class WorkoutSuggestionSerializer(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)
    suggestion = serializers.CharField(max_length=255)
