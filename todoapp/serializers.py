from rest_framework import serializers # type: ignore
from todoapp.models import Customer
from todoapp.models import Task

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Customer
        fields='__all__'



class TaskSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()

    class Meta:
        model=Task
        fields='__all__'

    def get_user_name(self, instance):
        return instance.user.full_name
    