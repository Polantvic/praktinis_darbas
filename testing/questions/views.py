from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
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
                  {'name': name, 'test': get_list_or_404(models.Question.objects.filter(test__name=name)),
                   'answers': get_list_or_404(models.Answer.objects.filter(test__name=name)),
                   'student_answers': models.StudentAnswer.objects.filter(student=request.user)})

def select_answer(request: HttpRequest, name: str, pk: int) -> HttpResponse:
    selected_answer = get_object_or_404(models.Answer, pk=pk)

    try:
        student_choice = get_object_or_404(models.StudentAnswer, student=request.user, question=selected_answer.question)
        if student_choice.answer == selected_answer:
            student_choice.delete()
        else:
            student_choice.answer = selected_answer
            student_choice.save()
    except:
        student_choice = models.StudentAnswer(student=request.user, question=selected_answer.question, answer=selected_answer)
        student_choice.save()

    return render(request, 'questions/test_questions.html',
            {'name': name, 'test': get_list_or_404(models.Question.objects.filter(test__name=name)),
            'answers': get_list_or_404(models.Answer.objects.filter(test__name=name)),
            'student_answers': models.StudentAnswer.objects.filter(student=request.user)})
