from .views import RegisterUserAPI,LoginUserAPI,HomeAPI,DetailBlogAPI,CommentAPI,SearchAPI
from django.urls import path
from rest_framework.authtoken import views

urlpatterns = [
    path('',HomeAPI.as_view()),

    path('register/',RegisterUserAPI.as_view()),
    # path('login/',LoginUserAPI.as_view()),

    path('login/', views.obtain_auth_token),
    
    path('detail/<slug:blog_id>/',DetailBlogAPI.as_view()),
    path('comment/<slug:blog_id>/',CommentAPI.as_view()),
    path('search/',SearchAPI.as_view()),
   


  


]