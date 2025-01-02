from django.urls import path
from .views import CategoryList, MediaFileList

urlpatterns = [
    path('api/categories/', CategoryList.as_view(), name='category_list'),
    path('api/media-files/', MediaFileList.as_view(), name='media_file_list'),
]
