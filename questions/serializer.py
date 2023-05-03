from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Question, Answer

#define serializer for the user model 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']#fields to be included in the serialized presentation

#serializer for question model
class QuestionSerializer(serializers.ModelSerializer):
    answers = serializers.PrimaryKeyRelatedField(many=True, read_only=True)#for related ansers
    user = UserSerializer(read_only=True)#for related to user

    class Meta:
        model = Question
        fields = ['id', 'title', 'content', 'created_at', 'user', 'answers']#fields to be included in the serialized representation

#serializer for answer model
class AnswerSerializer(serializers.ModelSerializer):
    question = serializers.PrimaryKeyRelatedField(
        queryset=Question.objects.all())
    user = UserSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'question', 'content', 'created_at', 'user']
