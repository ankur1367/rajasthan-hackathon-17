from django.conf.urls import url
from rest_framework import routers
from core.views import SchemeViewSet

router = routers.DefaultRouter()
router.register(r'scheme', SchemeViewSet)

urlpatterns = router.urls
