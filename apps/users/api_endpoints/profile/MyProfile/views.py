from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import UserSerializer


class MyProfileAPIView(RetrieveAPIView):
    """
    This endpoint retrieves the current user's profile.
    """

    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user


__all__ = ["MyProfileAPIView"]
