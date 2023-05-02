from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Answer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Question
        fields = ['id', 'title', 'content', 'created_at', 'user', 'answers']


class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all())
    user = UserSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'question', 'content', 'created_at', 'user']
