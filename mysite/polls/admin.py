from django.contrib import admin
from .models import Question, Choice

# Register your models here.

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('id', 'question_text', 'pub_date')

admin.site.register(Question,QuestionAdmin)