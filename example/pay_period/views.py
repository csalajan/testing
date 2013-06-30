from pay_period.models import PayPeriod
from pay_period.serializers import PayPeriodSerializer
from rest_framework import generics

class PayPeriodList(generics.ListCreateAPIView):
    queryset = PayPeriod.objects.all()
    serializer_class = PayPeriodSerializer

class PayPeriodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PayPeriod.objects.all()
    serializer_class = PayPeriodSerializer
