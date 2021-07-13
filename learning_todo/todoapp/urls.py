from django.urls import path
from . import views
from .views import TaskList

#urlpatterns = [
#    path('', TaskList.as_view(), name='tasks'),
#]


urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path("task-list/", views.tasklist, name='task-list'),
    path("task-detail/<str:pk>/", views.taskDetail, name='task-detail'),
]
