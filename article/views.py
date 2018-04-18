# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import datetime
from article import models

# Create your views here.
def home(request):
	posts = models.Article.objects.all()
	return render(request, 'home.html', locals())
	
