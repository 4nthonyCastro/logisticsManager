# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

# ================
# Model, Question
# ================
class Question(models.Model): 
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    # ================
    # Method, was_published_recently():
    # ================
    #   [Description]
    #       - Fixing the bug of was_published_recently() from returning True if its pub_date is in the future.
    #         Only returning True if the date is also in the past.
    # ================
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'

# ================
# Model, Choice
# ================
class Choice(models.Model): 
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
