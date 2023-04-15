from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('lesche.urls')),
    path('conversation/', include('conversation.urls')),
    path('admin/', admin.site.urls),
]
