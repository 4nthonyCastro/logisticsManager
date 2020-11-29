# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# This allows for the Polls app to be modified in Admin
from .models import Choice, Question

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
