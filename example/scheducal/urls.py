from django.conf.urls import (
        patterns, 
        url, 
        include,
    )
from rest_framework.urlpatterns import format_suffix_patterns
from scheducal.views import (
        user_views,
        workevent_views,
        category_views,
    )
from scheducal.views.reports import (
        time_sheet,
    )
 
urlpatterns = patterns('scheducal.views.workevent_views',
    url(r'^workevent/$', 
        workevent_views.WorkEventList.as_view(),
        name='workevent-list'),
    url(r'^workevent/(?P<pk>[0-9]+)/$', 
        workevent_views.WorkEventDetail.as_view(),
        name='workevent-detail'),
    url(r'^workevent/payperiod/(?P<pay_period>[0-9]+)/$', 
        workevent_views.WorkEventListForPayPeriod.as_view(),
        name='workevent-pay_periodlist'),
    url(r'^user/$', 
        user_views.UserList.as_view(),
        name='user-list'),
    url(r'^user/(?P<pk>[0-9]+)/$', 
        user_views.UserDetail.as_view(),
        name='user-detail'),
    url(r'^category/$', 
        category_views.CategoryList.as_view(),
        name='category-list'),
    url(r'^category/(?P<pk>[0-9]+)/$', 
        category_views.CategoryDetail.as_view(),
        name='category-detail'),
)

# Reports
urlpatterns += patterns('scheducal.views.reports.time_sheet',
    url(r'^report/timesheet/$', 'view'),
    url(r'^report/timesheet/(?P<payperiod_id>[0-9]+)/$', 'view'),
    url(r'^report/timesheet/user/(?P<user_id>[0-9]+)/$', 'view'),
    url(r'^report/timesheet/(?P<payperiod_id>[0-9]+)/user/(?P<user_id>[0-9]+)/$', 'view'),
)

urlpatterns = format_suffix_patterns(urlpatterns)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                                   namespace='rest_framework')),
    url(r'^api-token-auth/', 'rest_framework.authtoken.views.obtain_auth_token')
)
