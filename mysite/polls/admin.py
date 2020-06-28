from django.contrib import admin
from polls.models import Question, Choice # import 절대경로 polls.models <=> 상대경로 .models

admin.site.register(Question)
admin.site.register(Choice)
