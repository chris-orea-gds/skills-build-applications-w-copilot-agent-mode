"""octofit_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import views


# API root para navegación
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/users/',
        'teams': '/teams/',
        'activities': '/activities/',
        'leaderboard': '/leaderboard/',
        'workouts': '/workouts/',
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', api_root, name='api-root'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('teams/', views.TeamList.as_view(), name='team-list'),
    path('activities/', views.ActivityList.as_view(), name='activity-list'),
    path('leaderboard/', views.LeaderboardView.as_view(), name='leaderboard'),
    path('workouts/', views.WorkoutSuggestionList.as_view(), name='workout-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
