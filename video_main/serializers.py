from .models import VideoMain,Comment
from rest_framework import serializers

class VideoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoMain
        fields = ['id', 'title', 'author_name','view_number','uploaded_at']

class CommentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Comment
        fields = ['no', 'name', 'contents','number_of_likes','number_of_hates','author_like',
                  'created_at','updated_at']

class VideoUploadSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = VideoMain
        fields = ['id', 'title', 'descriptions', 'playlist', 'whether_to_disclose', 'viewer_age',
                  'age_limit']
