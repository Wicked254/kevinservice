from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from .models import Question, Answer
from .serializer import UserSerializer, QuestionSerializer, AnswerSerializer
from django.contrib.auth import authenticate, login
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class CreateUserView(generics.CreateAPIView):
    #View for creating a new user
    serializer_class = UserSerializer
class QuestionListCreateView(generics.ListCreateAPIView):
    #View for listing and creating questions
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]
# method to save the user making the request as the question's user.
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
class AnswerListCreateView(generics.ListCreateAPIView):
    #View for listing and creating answers
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        question_id = self.kwargs['question_id']
        return Answer.objects.filter(question_id=question_id)

    def perform_create(self, serializer):
        question_id = self.kwargs['question_id']
        question = Question.objects.filter(pk=question_id).first()
        if not question:
            raise ValidationError('Question not found')
        serializer.save(user=self.request.user, question=question)
class QuestionRetrieveView(generics.RetrieveAPIView):
    #View for retrieving a specific question
     queryset = Question.objects.all()
     serializer_class = QuestionSerializer


class UserQuestionsListView(generics.ListAPIView):
    """View for listing a user's questions"""
    serializer_class = QuestionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Question.objects.filter(user=user)


class UserRegistrationView(APIView):
    def post(self, request):
        email = request.data.get('email')
        username = request.data.get('username')
        password = request.data.get('password')

        if email is None or username is None or password is None:
            return Response({'error': 'Please provide all fields'}, status=status.HTTP_400_BAD_REQUEST)

        user = user.objects.create_user(
            email=email, username=username, password=password)
        Token.objects.create(user=user)

        return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)


class UserLoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'error': 'Please provide both username and password'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(username=username, password=password)

        if not user:
            return Response({'error': 'Invalid Credentials'}, status=status.HTTP_401_UNAUTHORIZED)

        token, _ = Token.objects.get_or_create(user=user)

        return Response({'token': token.key}, status=status.HTTP_200_OK)
