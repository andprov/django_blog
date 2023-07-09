from django.urls import path

from . import views

app_name = "blog"

urlpatterns = [
    # Главная.
    path(
        "",
        views.MainPostListView.as_view(),
        name="index",
    ),
    # Категория.
    path(
        "category/<slug:category_slug>/",
        views.CategoryPostListView.as_view(),
        name="category_posts",
    ),
    # Посты опубликованные определенным пользователем.
    # Для владельца страницы присутствует меню перехода на страницу
    # редактированию профиля и страницу смены пароля.
    path(
        "profile/<slug:username>/",
        views.UserPostsListView.as_view(),
        name="profile",
    ),
    # Пост.
    path(
        "posts/<int:pk>/",
        views.PostDetailView.as_view(),
        name="post_detail",
    ),
    # Редактировать профиля пользователя.
    path(
        "edit_profile/",
        views.UserProfileUpdateView.as_view(),
        name="edit_profile",
    ),
    # Создать пост.
    path(
        "posts/create/",
        views.PostCreateView.as_view(),
        name="create_post",
    ),
    # Редактировать пост.
    path(
        "posts/<int:pk>/edit/",
        views.PostUpdateView.as_view(),
        name="edit_post",
    ),
    # Удалить пост.
    path(
        "posts/<int:pk>/delete/",
        views.PostDeleteView.as_view(),
        name="delete_post",
    ),
    # Добавить комментарий.
    path(
        "posts/<int:pk>/comment/",
        views.CommentCreateView.as_view(),
        name="add_comment",
    ),
    # Редактировать комментарий.
    path(
        "posts/<int:pk>/edit_comment/<int:comment_pk>/",
        views.CommentUpdateView.as_view(),
        name="edit_comment",
    ),
    # Удалить комментарий
    path(
        "posts/<int:pk>/delete_comment/<int:comment_pk>/",
        views.CommentDeleteView.as_view(),
        name="delete_comment",
    ),
]
