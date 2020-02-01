from django import forms


class PostCreateForm(forms.Form):
    # views.py images = request.FILES.getlist('image')의 image
    image = forms.ImageField(
        widget=forms.ClearableFileInput(
            attrs={
                # 여러 개 이미지 한번에 업로드 가능하도록 함
                'multiple': True
            }))

    # views.py content = request.POST['content']의 content
    content = forms.CharField(
        widget=forms.Textarea()
    )


class CommentCreateForm(forms.Form):
    content = forms.CharField(
        max_length=10,
        widget=forms.Textarea()
    )

    def save(self, author, post):
        content = self.cleaned_data['content']
        post.postcomment_set.create(author=author, content=content)