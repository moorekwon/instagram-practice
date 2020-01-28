from django.shortcuts import render, redirect

from posts.forms import PostCreateForm
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


def post_create(request):
    if request.method == 'POST':
        author = request.user
        content = request.POST['content']
        # 여러 개의 이미지를 받음
        images = request.FILES.getlist('image')

        # 새 포스트 생성
        post = Post.objects.create(author=author, content=content)

        for image in images:
            post.postimage_set.create(image=image)

        print('post.postimage_set >>> ', post.postimage_set)
        # post일 경우, 포스트 생성하고 post-list 페이지로 이동
        return redirect('posts:post-list')
    else:
        # get일 경우, 포스트 생성 페이지로 이동
        form = PostCreateForm()

        context = {
            'form': form
        }
        return render(request, 'posts/post_create.html', context)


def post_ammend(request, pk):
    # 수정할 포스트 pk를 통하여 갖고 오기
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        # 수정할 때, 이전 content 불러와 input란에 보이게 하기
        post.content = request.POST['content']
        post.save()
        # post일 경우, 포스트 수정하고 post-list 페이지로 이동
        return redirect('posts:post-list')
    else:
        context = {
            'post': post
        }
        # get일 경우, 포스트 수정 페이지로 이동
        return render(request, 'posts/post_ammend.html', context)
