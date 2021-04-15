from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/post_delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/post_edit/', views.post_edit, name='post_edit'),
    path('<int:article_pk>/comments/new/', views.comments_new, name='comments_new'),
    path('<int:article_pk>/comments/<int:pk>/delete/', views.comments_delete, name='comments_delete'),
    path('<int:article_pk>/comments/<int:pk>/edit', views.comments_edit, name='comments_edit'),
]