from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout,login
# Create your views here.
from .models import Question,Answer,Quiz,MultipleQuestion
from .forms import QuestionForm, QuestionFormrawdjango, AnswerForm, QuizForm, ChooseQuizForm, Yesorno, QuizEditQuestion,ChooseQuizForAnswerForm, Createmultiplequestion




# def question_view(request):
	
# 	#quest = Question.objects.get(id=1)
	
# 	perguntas = []
	

# 	for i in (Question.objects.all()):
# 		perguntas.append(i.question_text)

# 	context = {
# 	'list' : perguntas
# 	}
# 	return render(request,"questions/question_view.html",context)


def quiz_view(request):    #Pagina que mostra todos os quizes e escolhes um para add pergutnas
	
	quizs = []
	for i in (Quiz.objects.all()):
		if i.quiz_id == request.user.username:
			quizs.append(i.quiz_name)

	my_form = ChooseQuizForm()
	if request.method == "POST":
		my_form = ChooseQuizForm(request.POST)
		if my_form.is_valid():
			#good data
			

			print(my_form.cleaned_data)
			for i in Quiz.objects.all():
				if i.quiz_name == my_form.cleaned_data["quiz_chosen"]:
					print(i.quiz_name)
					a=i
					if my_form.cleaned_data["action"] == "Add":
						return redirect("./" + str(i.quiz_name) + "addquestion")
					if my_form.cleaned_data["action"] == "Delete":	
						return redirect("./" + str(i.quiz_name) + "deletequestion")
					if my_form.cleaned_data["action"] == "Edit":
						return redirect("./" + str(i.quiz_name) + "editquestion")
		else:
			print(my_form.errors)	

	context = {
	'list' : quizs,
	'form' : my_form
	}
	return render(request,"questions/quiz_view.html",context)


def quiz_create_view(request):  #Add quizes
	Checkrepeat=False
	my_form = QuizForm()
	if request.method == "POST":
		my_form = QuizForm(request.POST)
		if my_form.is_valid():
			if request.user.is_authenticated:
				my_form.cleaned_data["quiz_id"] = request.user.username


			#good data
			for j in Quiz.objects.all():
				if j.quiz_name == my_form.cleaned_data["quiz_name"] :
					Checkrepeat=True

			print(my_form.cleaned_data)
			if Checkrepeat==False:
				Quiz.objects.create(**my_form.cleaned_data)
			


		else:
			print(my_form.errors)
		my_form = QuizForm()

		

		
	context = {
		'form': my_form,
		'Checkrepeat':Checkrepeat
	}
	return render(request, "questions/quiz_create.html",context)


# def question_create_view(request):
# 	form = QuestionForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()	
# 		form=QuestionForm()

# 	context1 = {
# 		'form': form
# 	}
# 	return render(request, "questions/question_create.html",context1)
	





# def question_create_viewrawdjango(request):
# 	my_form = QuestionFormrawdjango()
# 	if request.method == "POST":
# 		my_form = QuestionFormrawdjango(request.POST)
# 		if my_form.is_valid():
# 			#good data
# 			print(my_form.cleaned_data)
# 			Question.objects.create(**my_form.cleaned_data)

# 		else:
# 			print(my_form.errors)
# 		my_form = QuestionFormrawdjango()
# 	context3 = {
# 		'form': my_form
# 	}
# 	return render(request, "questions/question_create_rawdjango.html",context3)


# VER 2:49 para initial data




# def dynamic_lookup_view(request,my_id):
# 	obj = get_object_or_404(Question,id=my_id)
# 	per = get_object_or_404(Question,id=my_id).question_text

# 	my_form = AnswerForm()
# 	if request.method == "POST":
# 		my_form = AnswerForm(request.POST)
# 		if my_form.is_valid():
# 			#good data
# 			print(my_form.cleaned_data)
# 			my_form.cleaned_data['question_id']= my_id
# 			print(my_form.cleaned_data)
# 			Answer.objects.create(**my_form.cleaned_data)
# 			nextquestion=my_id+1
# 			ent = '../' + str(nextquestion)
# 			return redirect(ent)
# 		else:
# 			print(my_form.errors)



# 	context4 = {
# 		"object":obj,
# 		"pergunta":per,
# 		"form": my_form

# 	}

# 	return render(request, "questions/question_dynamicview.html",context4)




def quiz_create_question_view(request,my_quiz):

	quizatual = get_object_or_404(Quiz,quiz_name=my_quiz)
	my_form = QuestionFormrawdjango()

	if request.method == "POST":
		my_form = QuestionFormrawdjango(request.POST)
		if my_form.is_valid():
			#good data
			print(my_form.cleaned_data)
			#my_form.cleaned_data['questionquiz_id']= quizatual.id
			my_form.cleaned_data['questionquiz_key']= quizatual
			print(my_form.cleaned_data)
			Question.objects.create(**my_form.cleaned_data)
			my_form = QuestionFormrawdjango()

			
		else:
			print(my_form.errors)



	context4 = {
		
		"quiz":quizatual.quiz_name,
		"form": my_form

	}

	return render(request, "questions/quiz_create_question.html",context4)



def quiz_delete_question_view(request, my_quiz):
	quizatual = get_object_or_404(Quiz,quiz_name=my_quiz)
	perguntas=[]
	for i in Question.objects.filter(questionquiz_key=quizatual):
		perguntas.append(i.question_text)


	
	my_form = QuestionFormrawdjango()
	if request.method == "POST":
		my_form = QuestionFormrawdjango(request.POST)
		if my_form.is_valid():
			#le good data
			print(my_form.cleaned_data)
			Question.objects.filter(questionquiz_key=quizatual).filter(question_text=my_form.cleaned_data['question_text']).delete()
			my_form = QuestionFormrawdjango()

	context = {
		
		"list":perguntas,
		"form": my_form

	}

	return render(request, "questions/quiz_delete_question.html",context)



def quiz_edit_question_view(request,my_quiz):
	quizatual = get_object_or_404(Quiz,quiz_name=my_quiz)


	
	my_form = QuizEditQuestion()
	if request.method == "POST":
		my_form = QuizEditQuestion(request.POST)
		if my_form.is_valid():
			#le good data
			print(my_form.cleaned_data)
			questiontohange = Question.objects.filter(questionquiz_key=quizatual).filter(question_text=my_form.cleaned_data['oldquestion_text'])
			questiontohange.update(question_text = my_form.cleaned_data['newquestion_text'])
			my_form = QuizEditQuestion()



	
	perguntas=[]
	for i in Question.objects.filter(questionquiz_key=quizatual):
		perguntas.append(i.question_text)

	context = {
		
		"list":perguntas,
		"form": my_form

	}

	return render(request, "questions/quiz_edit_question.html",context)



def quiz_listtoanswer_view(request):    #Pagina que mostra todos os quizes e escolhes um para add pergutnas
	
	quizs = []
	for i in (Quiz.objects.all()):
		quizs.append(i.quiz_name)

	my_form = ChooseQuizForAnswerForm()
	if request.method == "POST":
		my_form = ChooseQuizForAnswerForm(request.POST)
		if my_form.is_valid():
			#good data
			print(my_form.cleaned_data)
			for i in Quiz.objects.all():
				if i.quiz_name == my_form.cleaned_data["quiz_name"]:
					print(i.quiz_name)
					return redirect("./" + str(i.quiz_name) + "answerquestion/"+ str(0))
		else:
			print(my_form.errors)	

	context = {
	'list' : quizs,
	'form' : my_form
	}
	return render(request,"questions/quiz_view.html",context)   #quiz_choosetoanswer.html tbm.. dá.. são iguais


def Answer_view(request,my_quiz,my_question):
	quizatual = Quiz.objects.filter(quiz_name = my_quiz)
	questoes = Question.objects.filter(questionquiz_key=quizatual[0])
	questaoatual = questoes[my_question]
	textodaquestao = questaoatual.question_text
	my_form = AnswerForm()
	if request.method == "POST":
		my_form = AnswerForm(request.POST)
		if my_form.is_valid():
			#good data
			print(my_form.cleaned_data)
			my_form.cleaned_data['answerquestion_id'] = questaoatual.questionquiz_id
			my_form.cleaned_data['answerquestion_key'] = questaoatual
			print(my_form.cleaned_data)
			Answer.objects.create(**my_form.cleaned_data)
			my_question=my_question+1

			ent = '../' + str(my_question)
			return redirect(ent)
		else:
			print(my_form.errors)



	context4 = {

		"pergunta" : textodaquestao,
		"form": my_form

	}

	return render(request, "questions/quiz_answer.html",context4)
	



def quiz_reviewanswerlist_view(request):    #Pagina que mostra todos os quizes e escolhes um para add pergutnas
	
	quizs = []
	for i in (Quiz.objects.all()):
		quizs.append(i.quiz_name)

	my_form = ChooseQuizForAnswerForm()
	if request.method == "POST":
		my_form = ChooseQuizForAnswerForm(request.POST)
		if my_form.is_valid():
			#good data
			

			print(my_form.cleaned_data)
			return redirect("../quiz/" + str(my_form.cleaned_data['quiz_name']) + "reviewanswer/")
		else:
			print(my_form.errors)	

	context = {
	'list' : quizs,
	'form' : my_form
	}
	return render(request,"questions/quiz_reviewanswer_list.html",context)










def answer_list_view(request,my_quiz):
	quizatual = Quiz.objects.filter(quiz_name = my_quiz)
	questoes = Question.objects.filter(questionquiz_key=quizatual[0])
	
	


	lista1 = []
	lista2 = []
	for i in questoes:
		lista1.append(i.question_text)
		
		stri = " "
		for j in Answer.objects.filter(answerquestion_key=i):
			stri =  stri + "  \n " + j.answer_text
		lista1.append(stri)


		context = {
		"questoes" : lista1,
		"respostas" : lista2

		}
	return render(request, "questions/quiz_question_answerlist.html",context)





def question_view_createmultipleanswer(request,my_quiz):
	quizatual = get_object_or_404(Quiz,quiz_name=my_quiz)
	my_form = Createmultiplequestion()

	if request.method == "POST":
		my_form = Createmultiplequestion(request.POST)
		if my_form.is_valid():
			#good data
			print(my_form.cleaned_data)
			#my_form.cleaned_data['questionquiz_id']= quizatual.id
			my_form.cleaned_data['questionquiz_key']= quizatual
			print(my_form.cleaned_data)
			MultipleQuestion.objects.create(**my_form.cleaned_data)
			my_form = Createmultiplequestion()

			
		else:
			print(my_form.errors)



	context4 = {
		
		"quiz":quizatual.quiz_name,
		"form": my_form

	}

	return render(request, "questions/quiz_create_multiplequestion.html",context4)




def logout_view(request):

		if request.method == "POST":
			 logout(request)

		return redirect("../")

def login_view(request):
		if request.method == "POST":

			form = AuthenticationForm(data=request.POST)
			
			if form.is_valid():
				user = form.get_user()
				login(request,user)

				return redirect("../")
		else:
			form=AuthenticationForm()
		return render(request,'questions/login.html',{'form':form})