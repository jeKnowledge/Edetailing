from django import forms

from .models import Question,Quiz

class QuestionForm(forms.ModelForm): #model para usar a meta
	question_text = forms.CharField(required=True, label='Escreve a tua pergunta', widget=forms.TextInput(attrs={"placeholder": "A tua questão"})) 
					#vai dar override na debaixo!
	class Meta:
		model = Question
		fields = [
			'question_text'
		]


	#SE EU QUISER QUE O INPUT TENHA UM CERTO STRING
	def clean_question_text(self,*args,**kwargs):
		question_text=self.cleaned_data.get("question_text")
		if "?" in question_text:
			return question_text
		else:
			raise forms.ValidationError("Isso não é uma pergunta")
		#2:46



class QuizForm(forms.Form):
	quiz_name = forms.CharField(required = True, label = 'Escreve o nome do quiz')
	quiz_id = forms.CharField(required = True, label = 'Escreve um ID')

class QuestionFormrawdjango(forms.Form):
	question_text = forms.CharField(required=True, label='Escreve a tua pergunta', widget=forms.TextInput(attrs={"placeholder": "A tua questão"})) #default é true anyways


class AnswerForm(forms.Form):
	answer_text = forms.CharField(required = True, label = 'Escreve a tua resposta')

class Yesorno(forms.Form):
	Yes_or_no = forms.BooleanField()

class ChooseQuizForm(forms.Form):
	quiz_chosen = forms.CharField(required = True, label = 'Escreve o nome do quiz que queres',widget=forms.TextInput(attrs={"placeholder": "Quiz"}))
	A =   (
		("Add", "Add"),
		("Edit", "Edit"),
		("Delete","Delete"),
		)
	action = forms.CharField(widget=forms.Select(choices=A), label = 'Mudar as questões:')

class QuizEditQuestion(forms.Form):
	oldquestion_text = forms.CharField(required=True, label='Qual queres editar?', widget=forms.TextInput(attrs={"placeholder": "Questão que queres mudar"})) 
	newquestion_text = forms.CharField(required=True, label='Passa a ser:', widget=forms.TextInput(attrs={"placeholder": "Nova questão"})) #default é true anyways

class ChooseQuizForAnswerForm(forms.Form):
	quiz_name = forms.CharField(required = True, label = 'Escreve o nome do quiz')

class MultipleQuestion(forms.Form):
	A =   (
		("1", "1"),
		("2", "2"),
		("3", "3"),
		("4", "4"),
		)
	action = forms.CharField(widget=forms.Select(choices=A), label = 'Reposta:')

class Createmultiplequestion(forms.Form):
	question_text = forms.CharField(required=True, label='Escreve a tua pergunta', widget=forms.TextInput(attrs={"placeholder": "A tua questão"}))
	answer1 = forms.CharField(required=False, label='Resposta', widget=forms.TextInput(attrs={"placeholder": "A tua questão"}))
	answer2 = forms.CharField(required=False, label='Resposta', widget=forms.TextInput(attrs={"placeholder": "A tua questão"}))
	answer3 = forms.CharField(required=False, label='Resposta', widget=forms.TextInput(attrs={"placeholder": "A tua questão"}))
	answer4 = forms.CharField(required=False, label='Resposta', widget=forms.TextInput(attrs={"placeholder": "A tua questão"}))
	A =   (
		("1", "1"),
		("2", "2"),
		("3", "3"),
		("4", "4"),
		)
	correctone = forms.CharField(widget=forms.Select(choices=A), label = 'Qual a correta?')