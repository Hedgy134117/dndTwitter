from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('twitter/', include('twitter.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
]
