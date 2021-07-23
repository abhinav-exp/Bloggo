from django.urls import path
from .views import *

urlpatterns = [
    path('', PostListView.as_view(), name = 'post_list'),
    path('about', AboutView.as_view(), name = 'about'),
    path('post/<int:pk>', PostDetailView.as_view(), name = 'post_detail'),
    path('post/new', CreatePostView.as_view(), name = 'post_new'),
    path('post/<int:pk>/edit', PostUpdateView.as_view(), name = 'post_edit'),
    path('post/<int:pk>/remove', PostDeleteView.as_view(), name = 'post_remove'),
    path('drafts', DraftListView.as_view(), name = 'post_draft_list'),
]