from django.urls import path
#from todoapp.views import UserViewSet, TaskViewSet
from rest_framework.routers import DefaultRouter # type: ignore
from todoapp.views import IsAccountAdminOrReadOnly, AccountViewSet


# user_list = UserViewSet.as_view({'get': 'list'})
# user_detail = UserViewSet.as_view({'get': 'retrieve'})
# task_list = TaskViewSet.as_view({'get': 'list'})
# task_detail = TaskViewSet.as_view({'get': 'retrieve'})


# urlpatterns = [
#     path('users/', user_list, name='user-list'),
#     path('users/<int:pk>/', user_detail, name='user-detail'),
#     path('task/', task_list, name='task-list'),
#     path('task/<int:pk>/', task_detail, name='task-detail'),
# ]



router = DefaultRouter()


urlpatterns = [
    path("IsAccountAdminOrReadOnly<int:pk>/", IsAccountAdminOrReadOnly, name="IsAccountAdminOrReadOnly"),
    path("AccountViewSet<int:pk>/", AccountViewSet.as_view({'get': 'list', 'post':'create'}), name="AccountViewSets"),
]
