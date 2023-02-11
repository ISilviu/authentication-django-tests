from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from django.conf import settings

class AuthenticationMixin:
    permission_classes = [
        permissions.IsAuthenticated if settings.ENABLE_AUTHENTICATION else permissions.AllowAny]

class UserViewSet(AuthenticationMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(AuthenticationMixin, viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
