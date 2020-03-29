from django.contrib import admin

from .models import Question
from .models import Choice

# class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=2

class QuestionAdmin(admin.ModelAdmin):
    # fields=['pub_date', 'question_text']
    fieldsets=[
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    inlines=[ChoiceInline]
    list_display=('question_text', 'pub_date', 'was_published_recently')

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
