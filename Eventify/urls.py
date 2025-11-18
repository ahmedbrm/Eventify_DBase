from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path("BIGBOSS/", admin.site.urls),
    path( '' , include('EventApp.urls')),
    
]
