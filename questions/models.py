from django.db import models
from django.contrib.auth.models import User
#defining a custom question model
class Question(models.Model):
    #link the question to the user who created it
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=257)#title field
    content = models.TextField()#this stores the text of the question
    created_at = models.DateTimeField(auto_now_add=True)#timestamp for creation of question
#return title when object is printed
    def __str__(self):
        return self.title

#defining the answer model
class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)#link the answer to user who created it 
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers')#link answer to the question it is associated with
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
#return content when object is printed
    def __str__(self):
        return self.content
