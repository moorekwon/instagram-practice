from django.shortcuts import render


def post_list(request):
    # request를 넘겨받아 render 호출
    # posts/post_list.html 템플릿을 보여줌
    return render(request, 'posts/post_list.html')
