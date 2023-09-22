from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import FileUploadView,FileListView

# Create a router and register our viewsets with it.
app_name = 'uploads'
urlpatterns = [
    path(r'upload/', FileUploadView.as_view(),name='upload'),
    path(r'files/', FileListView.as_view(),name='files'),

]
