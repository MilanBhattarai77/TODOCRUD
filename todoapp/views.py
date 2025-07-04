from django.shortcuts import render
from .models import Customer, Task
from django.shortcuts import get_object_or_404
from .serializers import CustomerSerializer, TaskSerializer
from rest_framework.response import Response # type: ignore
from rest_framework import viewsets # type: ignore
from rest_framework.decorators import api_view # type: ignore
from rest_framework.permissions import BasePermission, SAFE_METHODS # type: ignore

#Create your views here.

# class UserViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = Customer.objects.all()
#         serializer = CustomerSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Customer.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = CustomerSerializer(user)
#         return Response(serializer.data)
    







# class TaskViewSet(viewsets.ViewSet):
#     """
#     A simple ViewSet for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = Task.objects.all()
#         serializer = TaskSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = Task.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = TaskSerializer(user)
#         return Response(serializer.data)

    


class IsAccountAdminOrReadOnly(BasePermission):
    """
    Custom permission to only allow admins of an account to edit it.
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class AccountViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing accounts.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAccountAdminOrReadOnly]
    
    def get_queryset(self):
        """
        Optionally restricts the returned accounts to a given user,
        by filtering against a `user` query parameter in the URL.
        """
        queryset = self.queryset
        user = self.request.query_params.get('user', None)
        if user is not None:
            queryset = queryset.filter(user__id=user)
        return queryset