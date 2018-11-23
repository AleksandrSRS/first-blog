from django.db import models
import datetime
from django.utils import timezone

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name="Вопрос")
    pub_date = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = "Опубликавано недавно?"

    class Meta:
        verbose_name = "Опрос"
        verbose_name_plural = "Опросы"

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name="Варианты ответа")
    votes = models.IntegerField(default=0, verbose_name="Голосов")

    def __str__(self):
        return self.choice_text
