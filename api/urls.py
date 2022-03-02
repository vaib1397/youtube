from django.urls import path
from .views import *

urlpatterns = [
    path('videos', VideosListView.as_view()),
    path('videos/<str:video_id>', VideosListView.as_view()),

]