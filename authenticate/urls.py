from django.contrib import admin
from django.urls import path,include
# for rest framework 
from rest_framework import routers

from next.views import UserViewSet

router = routers.DefaultRouter()
router.register('users',UserViewSet)
# that ends here

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
    path('next/', include('next.urls')),
    path("api/", include(router.urls)),
]
