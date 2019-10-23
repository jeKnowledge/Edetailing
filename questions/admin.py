from django.contrib import admin

# Register your models here.

from .models import Question,Answer,Quiz,MultipleQuestion

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(MultipleQuestion)