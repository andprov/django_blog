from django.db import models
from django.contrib.auth import get_user_model

from core.models import BaseModel, BaseTitle

User = get_user_model()


class Location(BaseModel):
    """Местоположение.

    Атрибуты:
        - name: Название места.
    """

    name = models.CharField(
        max_length=256,
        verbose_name="Название места",
    )

    class Meta:
        verbose_name = "местоположение"
        verbose_name_plural = "Местоположения"
        ordering = ("name",)

    def __str__(self):
        return self.name


class Category(BaseModel, BaseTitle):
    """Категория.

    Атрибуты:
        - description: Описание категории.
        - slug: Идентификатор страницы для URL.
    """

    description = models.TextField(
        verbose_name="Описание",
    )
    slug = models.SlugField(
        unique=True,
        verbose_name="Идентификатор",
        help_text=(
            "Идентификатор страницы для URL; разрешены символы латиницы, "
            "цифры, дефис и подчёркивание."
        ),
    )

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "Категории"
        ordering = ("title",)

    def __str__(self):
        return self.title


class Post(BaseModel, BaseTitle):
    """Публикация.

    Атрибуты:
        - text: Текст публикации.
        - pub_date: Дата и время публикации, можно использовать будущие
        даты для отложенных публикаций.
        - author: Автор публикации.
        - location: Местоположение публикации, может быть пустым.
        - category: Категория публикации, может быть пустой.
        - image: Изображение публикации может быть пустым.
    """

    text = models.TextField(
        verbose_name="Текст",
    )
    pub_date = models.DateTimeField(
        verbose_name="Дата и время публикации",
        help_text=(
            "Если установить дату и время в будущем — можно делать "
            "отложенные публикации."
        ),
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор публикации",
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="Местоположение",
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Категория",
    )
    image = models.ImageField(
        upload_to="images",
        blank=True,
        verbose_name="Изображение",
    )

    class Meta:
        verbose_name = "публикация"
        verbose_name_plural = "Публикации"
        default_related_name = "posts"
        ordering = ("-pub_date",)

    def __str__(self):
        return self.title


class Comment(models.Model):
    """Комментарий.

    Атрибуты:
        - text: Текст комментария.
        - post: Пост, к которому относится комментарий.
        - author: Автор комментария.
        - created_at: Дата и время добавления комментария.
    """

    text = models.TextField(
        verbose_name="Комментарий",
    )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name="Пост",
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор",
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Добавлено",
    )

    class Meta:
        verbose_name = "комментарий"
        verbose_name_plural = "Комментарии"
        default_related_name = "comments"
        ordering = ("created_at",)

    def __str__(self):
        return f"Комментарий пользователя {self.author}"
