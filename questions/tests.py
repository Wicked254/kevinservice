from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from .models import Question, Answer
from .serializer import QuestionSerializer, AnswerSerializer


class QuestionTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com', password='testpass'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_question(self):
        url = reverse('question-list')
        data = {'title': 'Test question',
                'content': 'This is a test question.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(Question.objects.get().title, 'Test question')

    def test_retrieve_question(self):
        question = Question.objects.create(
            user=self.user, title='Test question', content='This is a test question.')
        url = reverse('question-detail', args=[question.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, QuestionSerializer(question).data)

    def test_list_questions(self):
        Question.objects.create(
            user=self.user, title='Test question 1', content='This is a test question.')
        Question.objects.create(
            user=self.user, title='Test question 2', content='This is another test question.')
        url = reverse('question-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(response.data[0]['title'], 'Test question 1')
        self.assertEqual(response.data[1]['title'], 'Test question 2')


class AnswerTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', email='testuser@test.com', password='testpass'
        )
        self.question = Question.objects.create(
            user=self.user, title='Test question', content='This is a test question.')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_create_answer(self):
        url = reverse('answer-list', args=[self.question.id])
        data = {'content': 'This is a test answer.'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Answer.objects.count(), 1)
        self.assertEqual(Answer.objects.get().content,
                         'This is a test answer.')

    def test_retrieve_answer(self):
        answer = Answer.objects.create(
            user=self.user, question=self.question, content='This is a test answer.')
        url = reverse('answer-detail', args=[self.question.id, answer.id])
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, AnswerSerializer(answer).data)

    def test_list_answers(self):
        Answer.objects.create(
            user=self.user, question=self.question, content='This is a test answer 1.')
        Answer.objects.create(
            user=self.user, question=self.question, content='This is another test answer.')
        url = reverse('answer-list', args=[self.question.id])
        response = self.client.get
