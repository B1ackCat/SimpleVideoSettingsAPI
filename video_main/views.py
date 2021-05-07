from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView,ListCreateAPIView

from .models import VideoMain,Comment
from .serializers import VideoSerializer,CommentSerializer,VideoUploadSerializer


class VideoList(ListAPIView):
    queryset = VideoMain.objects.all().order_by('-view_number')
    serializer_class = VideoSerializer

class CommentList(ListCreateAPIView):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer

class CommentEdit(RetrieveUpdateDestroyAPIView):
    lookup_field = 'no'
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class VideoEdit(RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    queryset = VideoMain.objects.all()
    serializer_class = VideoUploadSerializer

class VideoUpload(CreateAPIView):
    queryset = VideoMain.objects.all()
    serializer_class = VideoUploadSerializer