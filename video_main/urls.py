from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static

from . import views

app_name = 'video_main'

urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url('^$', views.VideoList.as_view(), name='video_list'), #index
    url(r'^VideoList/$', views.VideoList.as_view(), name='video_list'),  # list
    url(r'^VideoList/(?P<id>\d+)/$', views.VideoEdit.as_view(), name='video_edit'),  # edit
    url(r'^VideoList/(?P<id>\d+)/CommentList/$', views.CommentList.as_view(), name='comment_list'),  # comment list
    url(r'^VideoList/(?P<id>\d+)/CommentList/(?P<no>\d+)/$', views.CommentEdit.as_view(), name='comment'),  # comment list
    url(r'^VideoUpload/$', views.VideoUpload.as_view(), name='video_upload'), #list
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

