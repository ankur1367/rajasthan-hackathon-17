from django.conf.urls import url
from rest_framework import routers
from scheme.views import SchemeViewSet
from .views import InfoViewset, FamilyInfoViewset
router = routers.SimpleRouter()
router.register(r'info', InfoViewset)
router.register(r'familyinfo', FamilyInfoViewset)
router.register(r'scheme', SchemeViewSet)
urlpatterns = router.urls
