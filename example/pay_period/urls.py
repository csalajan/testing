from django.conf.urls import patterns, url, include
from rest_framework.urlpatterns import format_suffix_patterns
from pay_period import views

urlpatterns = patterns('pay_period.views',
    url(r'^payperiod/$', 
        views.PayPeriodList.as_view(),
        name='payperiod-list'),
    url(r'^payperiod/(?P<pk>[0-9]+)$', 
        views.PayPeriodDetail.as_view(),
        name='payperiod-detail'),
)

urlpatterns = format_suffix_patterns(urlpatterns)
