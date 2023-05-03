#importing all the necessary models
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from questions.views import CreateUserView, QuestionListCreateView, AnswerListCreateView, QuestionRetrieveView, UserQuestionsListView

#define the url patterns for the various API end points
urlpatterns = [
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),#for obtaining authentication token
    path('users/', CreateUserView.as_view(), name='user_create'),#allows user to create a new account
    path('questions/', QuestionListCreateView.as_view(),
         name='question_list_create'),#this end point allows user create and list questions
    path('questions/<int:pk>/', QuestionRetrieveView.as_view(),
         name='question_retrieve'),#allows user to retrieve a particular question with it's id
    path('questions/<int:question_id>/answers/',
         AnswerListCreateView.as_view(), name='answer_list_create'),#endpoint allows users to list and create answers for given question
    path('user/questions/', UserQuestionsListView.as_view(),#endpoint allows users to list questions asked by the user
         name='user_question_list'),
]
