from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_list_or_404, get_object_or_404
from . import models


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'tests_count': models.Test.objects.count(),
    }
    return render(request, 'questions/index.html', context)

def test_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'questions/test_list.html', {'test_list': models.Test.objects.all()})

def test_questions(request: HttpRequest, name: str) -> HttpResponse:
    return render(request, 'questions/test_questions.html',
                  {'test': get_list_or_404(models.Question.objects.filter(test__name=name)),
                   'answers': get_list_or_404(models.Answer.objects.all()), 'name': name})

def select_answer(request: HttpRequest, name: str, pk: int) -> HttpResponse:
    selected_answer = get_object_or_404(models.Answer, pk=pk)
    selected_answer.choice = not selected_answer.choice
    selected_answer.save()
    return render(request, 'questions/test_questions.html',
            {'test': get_list_or_404(models.Question.objects.filter(test__name=name)),
            'answers': get_list_or_404(models.Answer.objects.all()), 'name': name})
