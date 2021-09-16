from django.urls import path, include
from rest_framework import routers
from apps.lectures.views import LectureViewSet

router = routers.DefaultRouter()
router.register(r'', LectureViewSet)

urlpatterns = [
    path('', include(router.urls)),
]