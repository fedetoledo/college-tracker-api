from django.urls import path, include
from rest_framework import routers
from .viewsets import TodoViewSet, SubjectViewSet, ExamViewSet

router = routers.DefaultRouter()
router.register('todos', TodoViewSet)
router.register('subjects', SubjectViewSet)
router.register('exams', ExamViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
