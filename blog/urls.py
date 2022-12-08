from django.urls import path
from .views import render_post
from .views import post_detail

app_name='blog'

urlpatterns=[
    path('',render_post,name='post'),
    path('<int:post_id>', post_detail,name='post_detail') ,
]
