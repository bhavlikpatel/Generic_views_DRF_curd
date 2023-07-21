from django.urls import path
from . import views

urlpatterns = [
    path('api', views.UserApiList.as_view()),
    path('api/<int:pk>', views.UserApiDetail.as_view())
]
