from django.urls import path, re_path
from rest_framework_jwt.views import obtain_jwt_token

from . import views

urlpatterns = [
    path('signup/', views.UserSignUpView.as_view()),
    re_path(r'^username/(?P<username>\w+)/exist/$', views.UserExistView.as_view()),
    path('signin/', obtain_jwt_token)
]
