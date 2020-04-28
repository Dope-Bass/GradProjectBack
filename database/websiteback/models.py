from django.db import models
from .settings import DATE_INPUT_FORMATS


class Project(models.Model):
    title = models.CharField(max_length=120)
    founder = models.CharField(max_length=120, blank=True)
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)
    check_date = models.DateField(blank=True)
    design = models.BooleanField()
    functional = models.BooleanField()
    discussion = models.BooleanField()
    idea = models.BooleanField()
    bug = models.BooleanField()
    not_formal = models.BooleanField()
    description = models.TextField()
    stage = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Comment(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='comments')
    founder = models.CharField(max_length=120)
    date = models.DateField()
    text = models.TextField()

    def __str__(self):
        return self.text


class Participant(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='participant')
    user_name = models.CharField(max_length=120)

    def __str__(self):
        return self.user_name


class Message(models.Model):
    sender = models.CharField(max_length=120)
    receiver = models.CharField(max_length=120)
    title = models.CharField(max_length=120, default='Без Названия')
    date = models.DateField()
    text = models.TextField()

    def __str__(self):
        return self.text
