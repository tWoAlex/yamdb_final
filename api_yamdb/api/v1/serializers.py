from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from reviews.models import Category, Genre, Title, Review, Comment

User = get_user_model()


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitleSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(), slug_field='slug')
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(), slug_field='slug', many=True)
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = '__all__'

    def to_representation(self, instance):
        category = CategorySerializer().to_representation(instance.category)
        genre = GenreSerializer(many=True).to_representation(instance.genre)

        base = super().to_representation(instance)
        base['category'] = category
        base['genre'] = genre
        return base


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        fields = ('id', 'author', 'pub_date', 'score', 'text')
        model = Review

    def validate(self, data):
        if self.context['request'].method == 'POST':
            title_id = (
                self.context['request'].parser_context['kwargs']['title_id']
            )
            get_object_or_404(Title, pk=title_id)
            user = self.context['request'].user
            if user.reviews.filter().exists():
                raise serializers.ValidationError(
                    'На одно произведение можно оставлять только один отзыв')
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username')

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment


class RegistrationSerializer(serializers.ModelSerializer):
    def validate_username(self, value):
        if value.lower() == "me":
            raise serializers.ValidationError('Никнейм "me" запрещён')
        return value

    def run_validation(self, data):
        username = self.initial_data.get('username')
        email = self.initial_data.get('email')
        if not User.objects.filter(username=username, email=email).exists():
            super().run_validation(data)
        return data

    class Meta:
        fields = ('username', 'email')
        model = User


class TokenAproveSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name',
                  'last_name', 'bio', 'role')

    def update(self, instance, validated_data):
        validated_data.pop('role', None)
        return super().update(instance, validated_data)
