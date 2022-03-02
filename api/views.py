from api import serializers
from rest_framework import generics, mixins, filters
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from api.models import APIVideos
from django.shortcuts import get_object_or_404
from api.serializers import VideosSerializer
from api.utils import LimitSetPagination
# from django_filters.rest_framework import DjangoFilterBackend


class VideosListView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = VideosSerializer
    # permission_classes = (IsAuthenticated, )
    queryset = APIVideos.objects.all().order_by("-published_at")
    pagination_class = LimitSetPagination
    filter_backends = (filters.SearchFilter, )
    search_fields = ('title', 'description')


    def get(self, request, *args, **kwargs):
        if not "video_id" in kwargs:
            return self.list(request)
        post = get_object_or_404(APIVideos, video_id=kwargs["video_id"])
        return Response(VideosSerializer(post).data, status=200)