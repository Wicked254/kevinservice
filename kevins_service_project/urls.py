from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from questions.views import CreateUserView, QuestionListCreateView, AnswerListCreateView, QuestionRetrieveView, UserQuestionsListView


urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('users/', CreateUserView.as_view(), name='user_create'),
    path('questions/', QuestionListCreateView.as_view(),
         name='question_list_create'),
    path('questions/<int:pk>/', QuestionRetrieveView.as_view(),
         name='question_retrieve'),
    path('questions/<int:question_id>/answers/',
         AnswerListCreateView.as_view(), name='answer_list_create'),
    path('user/questions/', UserQuestionsListView.as_view(),
         name='user_question_list'),
]
