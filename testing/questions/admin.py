from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models


class TestAdmin(admin.ModelAdmin):
    list_display = ['name', 'lecturer', 'description']
    list_display_links = ['name']
    list_filter = ['lecturer']
    search_fields = ['name']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'all_answers', 'test']
    readonly_fields = ['all_answers']
    fieldsets = ((None, {"fields": ('test', 'text', 'all_answers')}),)

    def all_answers(self, obj: models.Question):
        return "; ".join(obj.answers.values_list('text', flat=True))


class AnswerAdmin(admin.ModelAdmin):
    list_display = ['text', 'choice', 'question']
    ordering = ['question']
    fieldsets = ((None, {"fields": ('test', 'question', 'text', 'choice')}),)


class StudentAnswerAdmin(admin.ModelAdmin):
    list_display = ['student', 'question', 'answer', 'result']
    readonly_fields = ['result']

    def result(self, obj: models.StudentAnswer):
        return obj.answer.choice


admin.site.register(models.Test, TestAdmin)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Answer, AnswerAdmin)
admin.site.register(models.StudentAnswer, StudentAnswerAdmin)
