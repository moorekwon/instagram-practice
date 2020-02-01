from django.urls import path

from . import views


app_name = 'posts'
# url 패턴 추가
urlpatterns = [
    # 루트 url에 post_list 뷰 할당
    # post-list 뷰를 식별하는 url 이름
    path('', views.post_list, name='post-list'),
    path('create/', views.post_create, name='post-create'),
    path('ammend/<int:pk>/', views.post_ammend, name='post-ammend'),
    path('<int:pk>/comments/create/', views.comment_create, name='comment-create')
]
