from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator

from .validators import correct_year

User = get_user_model()


class Category(models.Model):
    name = models.CharField(
        max_length=256, unique=True,
        verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Идентификатор')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name[:15]


class Genre(models.Model):
    name = models.CharField(
        max_length=256, unique=True,
        verbose_name='Название')
    slug = models.SlugField(unique=True, verbose_name='Идентификатор')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name[:15]


class Title(models.Model):
    category = models.ForeignKey(
        Category, null=True, on_delete=models.SET_NULL,
        related_name='titles', verbose_name='Категория'
    )
    genre = models.ManyToManyField(Genre, through='GenreTitle')
    name = models.CharField(max_length=256, verbose_name='Название')
    description = models.TextField(
        blank=True, null=True, verbose_name='Описание')
    year = models.SmallIntegerField(
        verbose_name='Год', db_index=True,
        validators=(correct_year,))

    class Meta:
        verbose_name = 'Произведение'
        verbose_name_plural = 'Произведения'

    def __str__(self):
        return self.name[:15]


class GenreTitle(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey(Title, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Связь произведения и его жанра'
        verbose_name_plural = 'Связи произведений и их жанров'

    def __str__(self):
        return f'{self.title_id}: {self.genre_id}'


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Произведение')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='reviews',
        verbose_name='Автор')
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True,
        db_index=True)
    text = models.TextField(verbose_name='Содержание')
    score = models.IntegerField(
        'Оценка',
        validators=(MaxValueValidator(10), MinValueValidator(1))
    )

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
        ordering = ['-pub_date']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'], name="unique_review")
        ]


class Comment(models.Model):
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField(
        'Дата публикации', auto_now_add=True, db_index=True)
    text = models.TextField()

    def __str__(self):
        return self.text[:15]
