from django.contrib import admin
from .models import Question, Choice

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 1
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']
    fieldsets = [
        (None,      {'fields': ['question_text']}),
        ('Дата',    {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInLine]
admin.site.register(Question, QuestionAdmin)

# admin.site.register(Choice)