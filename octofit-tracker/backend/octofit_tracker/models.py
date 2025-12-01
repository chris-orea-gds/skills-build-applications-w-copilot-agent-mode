
from djongo import models
from django.contrib.auth.models import User

# Modelo de equipo
class Team(models.Model):
	name = models.CharField(max_length=100)
	members = models.ArrayReferenceField(to=User, on_delete=models.CASCADE)

# Modelo de actividad
class Activity(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	type = models.CharField(max_length=100)
	duration = models.IntegerField()
	date = models.DateField()

# Modelo de sugerencia de entrenamiento
class WorkoutSuggestion(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	suggestion = models.CharField(max_length=255)

# El leaderboard se calcula dinámicamente, no requiere modelo persistente
