from django.shortcuts import render

from posts.models import Post


def post_list(request):
    # request를 넘겨받아 render 호출
    # posts/post_list.html 템플릿을 보여줌

    # 쿼리셋 이름으로 사용되는 posts 변수 만듦
    posts = Post.objects.all()

    # posts 쿼리셋 context에 담음
    context = {
        'posts': posts
    }

    # 템플릿을 사용하기 위한 context 매개변수 추가
    return render(request, 'posts/post_list.html', context)
