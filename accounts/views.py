from rest_framework.generics import CreateAPIView, RetrieveAPIView, ListAPIView
from .models import MyUser
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from .serializers import (
    UserCreateSerializer,
    UserDetailSerializer,
    UserLoginSerializer,
    UserListSerializer

)

from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin

class UserCreateAPIView(CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = MyUser.objects.all()

class UserDetailAPIView(RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = MyUser.objects.all()
    lookup_field = 'username'

class UserEditAPIView(DestroyModelMixin, UpdateModelMixin, RetrieveAPIView):
    serializer_class = UserDetailSerializer
    queryset = MyUser.objects.all()
    lookup_field = 'username'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)

class UserLoginAPIView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


class UserListAPIView(ListAPIView):
    serializer_class = UserListSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('position',)
    queryset = MyUser.objects.all()