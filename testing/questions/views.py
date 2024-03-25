from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
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
                  {'test': models.Question.objects.filter(test__name=name), 'name': name})
