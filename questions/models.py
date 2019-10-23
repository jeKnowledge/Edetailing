from django.db import models

# Create your models here.
class Quiz(models.Model):
	quiz_name= models.CharField(max_length=30)
	quiz_id= models.CharField(max_length=30,default=1)
	


class Question(models.Model):
    question_text = models.CharField(max_length=120)
    questionquiz_key = models.ForeignKey(Quiz, on_delete=models.CASCADE, default = 1)
   	#question_type = models.CharField(max_length=120)

class Answer(models.Model):
	answer_text = models.CharField(max_length=120)
	answerquestion_key = models.ForeignKey(Question, on_delete=models.CASCADE,  default = 1)

class MultipleChoice(models.Model):
	respostas = (
		("Add", "Add"),
		("Edit", "Edit"),
		("Delete","Delete"),
		)
	Res = models.CharField(max_length=30, choices = respostas)

class Predefinedanswer(models.Model):
	preanswer1 = models.CharField(max_length=120)
	preanswer2 = models.CharField(max_length=120)
	preanswer3 = models.CharField(max_length=120)
	preanswer4 = models.CharField(max_length=120)
	answerquestion_key = models.ForeignKey(Question, on_delete=models.CASCADE,  default = 1)


class MultipleQuestion(models.Model):
	question_text = models.CharField(max_length=120)
	answer1 = models.CharField(max_length=120)
	answer2 = models.CharField(max_length=120)
	answer3 = models.CharField(max_length=120)
	answer4 = models.CharField(max_length=120)
	correctone = models.CharField(max_length=120)
	questionquiz_key = models.ForeignKey(Quiz, on_delete=models.CASCADE, default = 1)