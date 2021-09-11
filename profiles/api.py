from profiles.models import Profiles
from rest_framework import viewsets, permissions 
from .serializers import ProfilesSerializer

# Profiles Viewset 
class ProfilesViewSet(viewsets.ModelViewSet):
  queryset = Profiles.objects.all() 
  permission_classes = [
    permissions.AllowAny
  ]
  serializer_class = ProfilesSerializer