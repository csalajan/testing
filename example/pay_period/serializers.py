from django.contrib.auth.models import User
from rest_framework import serializers
from pay_period.models import PayPeriod

class PayPeriodSerializer(serializers.HyperlinkedModelSerializer):
    work_event_list = serializers.HyperlinkedRelatedField(view_name='workevent-payperiod_list')
    class Meta:
        model = PayPeriod
        fields = ('url', 'name', 
                  'start', 'end',)
