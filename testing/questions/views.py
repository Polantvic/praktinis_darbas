from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_list_or_404, get_object_or_404
from . import models


def index(request: HttpRequest) -> HttpResponse:
    context = {
        'tests_count': models.Test.objects.count(),
        'user': request.user,
    }
    return render(request, 'questions/index.html', context)

def test_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'questions/test_list.html', {'test_list': models.Test.objects.all()})

def test_questions(request: HttpRequest, name: str) -> HttpResponse:
    studentesult = models.StudentResult.objects.filter(student=request.user, test__name=name).first()

    if studentesult is not None:
        return render(request, 'questions/student_result.html',
                {'user': request.user, 'result': studentesult.result,
                'questions': studentesult.amount_questions})
                                        
    return render(request, 'questions/test_questions.html',
                  {'name': name, 'user': request.user,
                   'test': get_list_or_404(models.Question.objects.filter(test__name=name)),
                   'answers': get_list_or_404(models.Answer.objects.filter(test__name=name)),
                   'student_answers': models.StudentAnswer.objects.filter(student=request.user)})

def select_answer(request: HttpRequest, name: str, pk: int) -> HttpResponse:
    selected_answer = get_object_or_404(models.Answer, pk=pk)

    def is_correct_choice(selected_answer):
            if selected_answer.choice == True:
                return True
            else:
                return False

    try:
        student_choice = get_object_or_404(models.StudentAnswer, student=request.user, question=selected_answer.question)
        if student_choice.answer == selected_answer:
            student_choice.delete()
        else:
            student_choice.answer = selected_answer
            student_choice.is_correct = is_correct_choice(selected_answer)
            student_choice.save()
    except:
        student_choice = models.StudentAnswer(student=request.user, question=selected_answer.question,
                                              answer=selected_answer, is_correct=is_correct_choice(selected_answer))
        student_choice.save()

    return render(request, 'questions/test_questions.html',
            {'name': name, 'user': request.user,
             'test': get_list_or_404(models.Question.objects.filter(test__name=name)),
            'answers': get_list_or_404(models.Answer.objects.filter(test__name=name)),
            'student_answers': models.StudentAnswer.objects.filter(student=request.user)})

def student_result(request: HttpRequest, name: str) -> HttpResponse:
    student_answers = models.StudentAnswer.objects.filter(student=request.user, answer__test__name=name)
    true_answers = models.Answer.objects.filter(test__name=name, choice=True)
    questions = models.Question.objects.filter(test__name=name)
    amount_questions = questions.count()
    result = 0

    for question in questions:
        student_answer = student_answers.filter(question=question).first()
        true_answer = true_answers.filter(question=question).first()
        if student_answer is not None:
            if student_answer.answer == true_answer:
                result += 1

    test = models.Test.objects.filter(name=name).first()
    current_student_result = models.StudentResult(student=request.user, test=test, is_done=True,
                                                  result=result, amount_questions=amount_questions)
    current_student_result.save()

    return render(request, 'questions/student_result.html',
                  {'user': request.user, 'result': current_student_result.result,
                   'questions': current_student_result.amount_questions})
