from django.urls import include, path
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'manuscripts', ManuscriptViewSet)
router.register(r'save', SaveManuscriptView)

urlpatterns = [
    path('manuscript/', include(router.urls)),
    path('manuscript/', include(router.urls)),
]
