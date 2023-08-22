from django.urls import path
from .views import CustomRetrieveAPIView

urlpatterns = [
    path('test', CustomRetrieveAPIView.as_view())
]