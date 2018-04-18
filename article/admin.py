# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from article import models

class ArticleAdmin(admin.ModelAdmin):
	list_display = ['id', 'title', 'category', 'datetime']
	ordering = ('id',)

admin.site.register(models.Article, ArticleAdmin)
