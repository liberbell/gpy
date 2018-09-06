from django.contrib import admin
from .models import Choice, Question

# Register your models here.
# admin.site.register(Question)

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title',            {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
