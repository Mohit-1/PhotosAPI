from django.contrib import admin
from django.urls import path, include
from photos.views import ListGroups, ListPhotoForGroup, PhotoDetails

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('rest_auth.urls')),
    path('api/v1/groups/', ListGroups.as_view()),
    path('api/v1/group/<str:gid>/', ListPhotoForGroup.as_view()),
    path('api/v1/photo/<int:pid>/', PhotoDetails.as_view())
]
