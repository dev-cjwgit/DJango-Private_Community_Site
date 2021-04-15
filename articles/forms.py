from django import forms
from .models import Article, Comment


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        max_length=100,
        label='제목',
        widget=forms.TextInput(
            attrs={
                'class': 'title',
                'placeholder': '제목을 입력하세요.',
            }
        )
    )
    content = forms.CharField(
        max_length=50,
        label='내용',
        widget=forms.Textarea(
            attrs={
                'class': 'content',
                'placeholder': '댓글을 입력해주세요.',
            }
        )
    )

    class Meta:
        model = Article
        fields = ('title', 'content',)


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        max_length=100,
        label='내용',
        widget=forms.TextInput(
            attrs={
                'class': 'content',
                'size': '81',
            }
        )
    )

    class Meta:
        model = Comment
        fields = ('content',)

# class ArticleForm(forms.Form):
#     title = forms.CharField(
#         max_length=10,
#         label='제목',
#         widget=forms.TextInput(
#             attrs={
#                 'class': 'title',
#                 'placeholder': '제목을 입력하세요.',
#             }
#         )
#     )
#     content = forms.CharField(
#         label='내용',
#         widget=forms.Textarea(
#             attrs={
#                 'class': 'content',
#                 'rows': 5,
#                 'cols': 20,
#             }
#         )
#     )
