from django.contrib.auth.models import User, Group
from rest_framework import serializers


class User Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = GroupSerializerfields = ['url', 'name']
