import re

from django.contrib.auth.models import User
from django.db import models


# 모델 정의하기
class Post(models.Model):
    TAG_PATTERN = re.compile(r'#(\w+)')

    tags = models.ManyToManyField(
        'Tag',
        verbose_name='해시태그 목록',
        related_name='posts',
        blank=True
    )

    # ForeignKey 다른 모델에 대한 링크
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    # TextField 글자 수 제한 없는 텍스트
    content = models.TextField()
    content_html = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-pk',)

    # Post 모델의 author, created 속성을 string 형태로 호출
    def __str__(self):
        return f'{self.author} | {self.created}'

    def _save_html(self):
        self.content_html = re.sub(
            self.TAG_PATTERN,
            r'<a href="/explore/tags/\g<1>/">#\g<1></a>',
            self.content
        )

    def _save_tags(self):
        # re.findall(찾을 문자열, 찾을 곳)
        tag_name_list = re.findall(self.TAG_PATTERN, self.content)
        tags = [Tag.objects.get_or_create(name=tag_name)[0] for tag_name in tag_name_list]
        self.tags.set(tags)

    def save(self, *args, **kwargs):
        # post 생성하기 전 html 형태 만들기
        self._save_html()
        # 저장
        super().save(*args, **kwargs)
        # 저장된 post에서 tag 찾기
        self._save_tags()


class PostImage(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # .media/posts/images 안에 저장
    image = models.ImageField(upload_to='posts/images')


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    class Meta:
        ordering = ('-pk',)


class Tag(models.Model):
    name = models.CharField('태그명', max_length=100)

    def __str__(self):
        return self.name
