from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views import View

from blog.models import Comment
from core.utils import get_post_data


class CommentMixinView(LoginRequiredMixin, View):
    """Mixin для редактирования и удаления комментария.

    Атрибуты:
        - model: Класс модели, используемой для комментариев.
        - template_name: Имя шаблона, используемого для отображения страницы.
        - pk_url_kwarg: Имя URL-параметра, содержащего идентификатор
        комментария.

    Методы:
        - dispatch(request, *args, **kwargs): Проверяет, является ли
        пользователь автором комментария.
        - get_success_url(): Возвращает URL-адрес перенаправления после
        успешного редактирования или удаления комментария.
    """

    model = Comment
    template_name = "blog/comment.html"
    pk_url_kwarg = "comment_pk"

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().author != request.user:
            return redirect("blog:post_detail", pk=self.kwargs["pk"])
        get_post_data(self.kwargs)
        return super().dispatch(request, *args, **kwargs)

    def get_success_url(self):
        pk = self.kwargs["pk"]
        return reverse("blog:post_detail", kwargs={"pk": pk})
