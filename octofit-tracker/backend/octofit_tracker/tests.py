from django.test import TestCase
from django.contrib.auth.models import User
from .models import Team, Activity, WorkoutSuggestion

class UserModelTest(TestCase):
    def test_create_user(self):
        user = User.objects.create_user(username='testuser', password='testpass')
        self.assertEqual(user.username, 'testuser')

class TeamModelTest(TestCase):
    def test_create_team(self):
        user = User.objects.create_user(username='member', password='pass')
        team = Team.objects.create(name='Test Team')
        team.members.add(user)
        self.assertEqual(team.name, 'Test Team')
        self.assertIn(user, team.members.all())

class ActivityModelTest(TestCase):
    def test_create_activity(self):
        user = User.objects.create_user(username='activityuser', password='pass')
        activity = Activity.objects.create(user=user, type='Running', duration=30, date='2025-12-01')
        self.assertEqual(activity.type, 'Running')

class WorkoutSuggestionModelTest(TestCase):
    def test_create_suggestion(self):
        user = User.objects.create_user(username='suggestuser', password='pass')
        suggestion = WorkoutSuggestion.objects.create(user=user, suggestion='Try HIIT')
        self.assertEqual(suggestion.suggestion, 'Try HIIT')
