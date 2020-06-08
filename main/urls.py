from django.urls import path, include
from main import views
urlpatterns=[
    path('',views.User.as_view(),name='user'),
    path('auth=1/',views.Asdw.as_view(), name="auth")
]