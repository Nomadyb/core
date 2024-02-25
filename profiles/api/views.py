from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from profiles.models import Profile
from profiles.api.serializers import ProfilSerializer



class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfilSerializer
    permission_classes = [IsAuthenticated]
    