from django.conf.urls.defaults import patterns, url
from django.contrib.auth.decorators import login_required

from .views import EntryCreateView, EntryUpdateView, DetailView, \
    VoteCreateView, VoteListView, VoteDeleteView, EntryDeleteView, \
    EntryDisableView

urlpatterns = patterns('',
    url(r'^(?P<pk>\d+)/edit/$', login_required(EntryUpdateView.as_view()), name='edit'),
    url(r'^(?P<pk>\d+)/vote/$', login_required(VoteCreateView.as_view()), name='vote'),
    url(r'^(?P<pk>\d+)/delete/$', login_required(EntryDeleteView.as_view()), name='delete'),
    url(r'^(?P<pk>\d+)/disable/$', login_required(EntryDisableView.as_view()), name='disable'),
    url(r'^(?P<pk>\d+)/play/(?P<slug>[-\w]+)/$', DetailView.as_view(), name='play'),
    url(r'^new/$', login_required(EntryCreateView.as_view()), name='new'),
    url(r'^votes/$', login_required(VoteListView.as_view()), name='votes'),
    url(r'^votes/(?P<pk>\d+)/delete/$', login_required(VoteDeleteView.as_view()), name='votes_delete'),
)
