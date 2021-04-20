from django.urls import path,re_path

from . import views

urlpatterns = [
    path('users/', views.UserSignUpView.as_view()),
    re_path(r'^users/(?P<username>\w{5,32})/exist/$', views.UserExistView.as_view())
]
