from rest_framework import serializers
from uploading.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['facebook_post','photo']