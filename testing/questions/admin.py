from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from . import models


class TestAdmin(admin.ModelAdmin):
    list_display = ['name', 'lecturer', 'description']
    list_display_links = ['name']
    list_filter = ['lecturer']
    search_fields = ['name']


class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'answers', 'test']
    readonly_fields = ['answers']
    fieldsets = ((None, {"fields": ('test', 'text', 'answers')}),)

    def answers(self, obj: models.Question):
        return "; ".join(obj.options.values_list('text', flat=True))


class OptionAdmin(admin.ModelAdmin):
    pass


class StudentAnswerAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Test, TestAdmin)
admin.site.register(models.Question, QuestionAdmin)
admin.site.register(models.Option, OptionAdmin)
admin.site.register(models.StudentAnswer, StudentAnswerAdmin)
