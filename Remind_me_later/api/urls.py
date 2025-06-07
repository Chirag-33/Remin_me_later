from django.urls import path
from .views import RemindCreateView

urlpatterns = [
    path('create/', RemindCreateView.as_view(), name='create-reminder'),
]
