"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

# url 넣기
urlpatterns = [
    # admin/으로 시작하는 모든 url을 views.py에서 찾음
    path('admin/', admin.site.urls),
    # posts.urls로 요청을 전송
    path('', include('posts.urls'))
]

urlpatterns += static(
    # MEDIA_URL(/media/) 경로로 들어오면
    prefix=settings.MEDIA_URL,
    # MEDIA_ROOT(.media) 폴더에서 이미지 리턴
    document_root=settings.MEDIA_ROOT
)
