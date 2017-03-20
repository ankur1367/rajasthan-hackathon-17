from rest_framework import viewsets
from .models import Info, FamilyInfo
from .serializers import InfoSerializer, FamilyInfoSerializer

class InfoViewset(viewsets.ModelViewSet):
    queryset = Info.objects.all()
    serializer_class = InfoSerializer

class FamilyInfoViewset(viewsets.ModelViewSet):
    queryset = FamilyInfo.objects.all()
    serializer_class = FamilyInfoSerializer
