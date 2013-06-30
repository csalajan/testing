from django.contrib.auth.models import User
from rest_framework import serializers
from scheducal.models import (
        WorkEvent,
        ScheduleEvent,
        Category,
    )

class SaveWorkEventSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    duration = serializers.Field(source='duration')

    class Meta:
        model = WorkEvent
        fields = ('url', 'category',
                  'start_time', 'end_time',
                  'start_date', 'comments',
                  'on_campus',)

class ViewWorkEventSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.Field(source='owner.username')
    duration = serializers.Field(source='duration')

    class Meta:
        model = WorkEvent
        fields = ('url', 'user', 'category',
                  'start_time', 'end_time',
                  'start_date', 'comments',
                  'on_campus',)
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    work_event = serializers.HyperlinkedRelatedField(many=True, view_name='work_event-detail')
    class Meta:
        model = User
        fields = ('url', 'username',
                  'first_name', 'last_name',)

class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('url', 'name', 'is_project',)
