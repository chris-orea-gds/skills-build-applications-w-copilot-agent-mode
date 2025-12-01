from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSuggestionSerializer

# Simulación de datos para equipos, actividades, leaderboard y sugerencias
# En una app real, estos vendrían de la base de datos MongoDB

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

class TeamList(APIView):
    def get(self, request):
        # Simulación de equipos
        teams = [
            {'id': '1', 'name': 'Team Alpha', 'members': []},
            {'id': '2', 'name': 'Team Beta', 'members': []},
        ]
        serializer = TeamSerializer(teams, many=True)
        return Response(serializer.data)

class ActivityList(APIView):
    def get(self, request):
        # Simulación de actividades
        activities = [
            {'id': '1', 'user': None, 'type': 'Running', 'duration': 30, 'date': '2025-12-01'},
        ]
        serializer = ActivitySerializer(activities, many=True)
        return Response(serializer.data)

class LeaderboardView(APIView):
    def get(self, request):
        leaderboard = [
            {'user': None, 'total_duration': 120},
        ]
        serializer = LeaderboardSerializer(leaderboard, many=True)
        return Response(serializer.data)

class WorkoutSuggestionList(APIView):
    def get(self, request):
        suggestions = [
            {'id': '1', 'user': None, 'suggestion': 'Try HIIT for 20 minutes'},
        ]
        serializer = WorkoutSuggestionSerializer(suggestions, many=True)
        return Response(serializer.data)
