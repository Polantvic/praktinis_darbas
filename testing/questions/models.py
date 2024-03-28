from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class Test(models.Model):
    name = models.CharField(_("name"), max_length=100, db_index=True)
    description = models.CharField(_("description"), blank=True, max_length=500)
    lecturer = models.ForeignKey(get_user_model(), verbose_name=_("lecturer"),
                                 on_delete=models.CASCADE, related_name='tests')

    class Meta:
        verbose_name = _("test")
        verbose_name_plural = _("tests")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("test_detail", kwargs={"pk": self.pk})


class Question(models.Model):
    text = models.CharField(_("text"), max_length=500, db_index=True)
    test = models.ForeignKey(Test, verbose_name=_("test"), on_delete=models.CASCADE,
                             related_name="questions")

    class Meta:
        verbose_name = _("question")
        verbose_name_plural = _("questions")

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("question_detail", kwargs={"pk": self.pk})


class Answer(models.Model):
    text = models.CharField(_("text"), max_length=500, db_index=True)
    choice = models.BooleanField(_("choice"), default=False, db_index=True)
    question = models.ForeignKey(Question, verbose_name=_("question"),
                                 on_delete=models.CASCADE, related_name="answers")
    test = models.ForeignKey(Test, verbose_name=_("test"), on_delete=models.CASCADE,
                             related_name="answers")

    class Meta:
        verbose_name = _("answer")
        verbose_name_plural = _("answers")

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse("answer_detail", kwargs={"pk": self.pk})


class StudentAnswer(models.Model):
    student = models.ForeignKey(get_user_model(), verbose_name=_("student"),
                                on_delete=models.CASCADE, related_name="studentanswers")
    question = models.ForeignKey(Question, verbose_name=_("question"),
                                 on_delete=models.CASCADE, related_name="studentanswers")
    answer = models.ForeignKey(Answer, verbose_name=_("answer"),
                               on_delete=models.CASCADE, related_name="studentanswers")
    is_correct = models.BooleanField(_("is_correct"), default=False)

    class Meta:
        verbose_name = _("studentanswer")
        verbose_name_plural = _("studentanswers")

    def __str__(self):
        return self.answer.text

    def get_absolute_url(self):
        return reverse("studentanswer_detail", kwargs={"pk": self.pk})


class StudentResult(models.Model):
    student = models.ForeignKey(get_user_model(), verbose_name=_("student"),
                                on_delete=models.CASCADE, related_name="studentresults")
    test = models.ForeignKey(Test, verbose_name=_("test"), on_delete=models.CASCADE,
                             related_name="studentresults")
    is_done = models.BooleanField(_("is_done"), default=False, db_index=True)
    result = models.IntegerField(_("result"), default=-1)
    amount_questions = models.SmallIntegerField(_("amount_questions"), default=0)

    class Meta:
        verbose_name = _("studentresult")
        verbose_name_plural = _("studentresults")

    def __str__(self):
        return self.result

    def get_absolute_url(self):
        return reverse("studentresult_detail", kwargs={"pk": self.pk})
