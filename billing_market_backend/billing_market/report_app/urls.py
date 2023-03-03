from django.urls import path
from .views import ReportsAPIView

urlpatterns = [
    path('daily/', ReportsAPIView.as_view())
]