# vim: tabstop=4 shiftwidth=4 softtabstop=4

#    Copyright 2013, Big Switch Networks, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from django.conf.urls.defaults import url, patterns

from .views import IndexView
from .views import AddPoolView, AddMemberView, AddMonitorView, AddVipView
from .views import (UpdatePoolView, UpdateMemberView,
                    UpdateVipView, UpdateMonitorView)
from .views import PoolDetailsView, VipDetailsView
from .views import MemberDetailsView, MonitorDetailsView

urlpatterns = patterns(
    'openstack_dashboard.dashboards.project.loadbalancers.views',
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^addpool$', AddPoolView.as_view(), name='addpool'),
    url(r'^updatepool/(?P<pool_id>[^/]+)/$',
        UpdatePoolView.as_view(), name='updatepool'),
    url(r'^addvip/(?P<pool_id>[^/]+)/$', AddVipView.as_view(), name='addvip'),
    url(r'^updatevip/(?P<vip_id>[^/]+)/$',
        UpdateVipView.as_view(), name='updatevip'),
    url(r'^addmember$', AddMemberView.as_view(), name='addmember'),
    url(r'^updatemember/(?P<member_id>[^/]+)/$',
        UpdateMemberView.as_view(), name='updatemember'),
    url(r'^addmonitor$', AddMonitorView.as_view(), name='addmonitor'),
    url(r'^updatemonitor/(?P<monitor_id>[^/]+)/$',
        UpdateMonitorView.as_view(), name='updatemonitor'),
    url(r'^pool/(?P<pool_id>[^/]+)/$',
        PoolDetailsView.as_view(), name='pooldetails'),
    url(r'^vip/(?P<vip_id>[^/]+)/$',
        VipDetailsView.as_view(), name='vipdetails'),
    url(r'^member/(?P<member_id>[^/]+)/$',
        MemberDetailsView.as_view(), name='memberdetails'),
    url(r'^monitor/(?P<monitor_id>[^/]+)/$',
        MonitorDetailsView.as_view(), name='monitordetails'))
