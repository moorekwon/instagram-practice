from django.urls import path

from . import views

# url 패턴 추가
urlpatterns = [
    # 루트 url에 post_list 뷰 할당
    # post-list 뷰를 식별하는 url 이름
    path('', views.post_list, name='post-list')
]
