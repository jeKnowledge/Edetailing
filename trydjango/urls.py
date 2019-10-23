"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include
from django.conf.urls import url
from users import views as core_views
from django.contrib import admin
from django.urls import path
from pages.views import home_view
from questions.views import login_view,logout_view,quiz_reviewanswerlist_view,answer_list_view,Answer_view,quiz_listtoanswer_view, quiz_edit_question_view, quiz_delete_question_view,quiz_create_question_view,quiz_view,quiz_create_view,question_view_createmultipleanswer
urlpatterns = [
   # path('question/', question_view, name='question'),
    path('', home_view, name='home'),
    path('admin/', admin.site.urls),
   # path('create/',question_create_view),
   # path('createrawdjango/',question_create_viewrawdjango),
   # path('questiondynamic/<int:my_id>/',dynamic_lookup_view),
    path('quizcreate/', quiz_create_view),
    path('quiz/', quiz_view),
    path('quiz/<str:my_quiz>addquestion/',quiz_create_question_view),
    path('quiz/<str:my_quiz>addquestionmultiple/',question_view_createmultipleanswer),
    path('quiz/<str:my_quiz>deletequestion/',quiz_delete_question_view),
    path('quiz/<str:my_quiz>editquestion/',quiz_edit_question_view),
    path('quizchoosetoanswer/',quiz_listtoanswer_view),
    path('quizchoosetoanswer/<str:my_quiz>answerquestion/<int:my_question>/',Answer_view),
    url(r'^signup/$', core_views.signup, name='signup'),
    url(r'^logout/$', logout_view, name='logout'),
    url(r'^login/$',login_view,name = "login"),
    path('quiz/<str:my_quiz>reviewanswer/',answer_list_view),
    path('reviewlistanswer/',quiz_reviewanswerlist_view),
    path('accounts/', include('django.contrib.auth.urls'))
    ]