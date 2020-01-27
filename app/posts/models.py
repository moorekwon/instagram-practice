from django.contrib.auth.models import User
from django.db import models


# 모델 정의하기
class Post(models.Model):
    # ForeignKey 다른 모델에 대한 링크
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # TextField 글자 수 제한 없는 텍스트
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    # Post 모델의 author, created 속성을 string 형태로 호출
    def __str__(self):
        return f'{self.author} | {self.created}'
